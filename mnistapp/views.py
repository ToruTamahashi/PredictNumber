from django.shortcuts import render
from PIL import Image
import numpy as np
import pickle
from django.conf import settings
from sklearn import preprocessing
#from sklearn.neural_network import MLPClassifier

# Create your views here.
def mnistfunc(request):
    #リクエストがPOSTだったら
    if request.method == 'POST':
        try:
            # 画像化して処理
            #img_moto =Image.open(request.FILES['image'])
            #img=numpy.asarray(numpy.array(img_moto))
            #print(img)
            
            #im_gray = np.array(Image.open(request.FILES['image']).convert('L'))# 出力画像用の配列生成
            #im_gray = np.array(Image.open(settings.MEDIA_ROOT + '/image_5_2.jpg').convert('L'))
            #im_gray = np.array(Image.open(request.POST['img']).convert('L'))
            im_gray_str = request.POST['img']
            im_gray_1Dlist = im_gray_str.split(',')
            
            im_gray_2Dlist = np.zeros((28, 28))
            size = 28*28
            count = 0
            row = 0
            for i in range(size):
                im_gray_2Dlist[row][count]= im_gray_1Dlist[i]
                count = count+1
                if count == 28:
                    count =0
                    row = row + 1
                    

            im_gray = im_gray_2Dlist

            print(im_gray.shape)
            #print(im.shape)

            threshold_img = im_gray.copy()
            # 閾値
            threshold_value = 127

            # 方法1（NumPyで実装）
            threshold_img[im_gray > threshold_value] = 0
            threshold_img[im_gray <= threshold_value] = 255
            a = threshold_img.reshape(784,)
            b = preprocessing.minmax_scale(a)
            c = a.reshape(1,784)
            
            #mediaディレクトリにアクセスする
            with open(settings.MEDIA_ROOT + '/model6.pickle', mode='rb') as fp:
                clf = pickle.load(fp)
            print("e")
            print(clf.predict(c))
            print(np.argmax(clf.predict(c)))
          
            answer = str(np.argmax(clf.predict(c)))

            return render(request, 'mnist.html', {'answer':answer})
        except:
            #一致するものがなければ（エラーを吐くので）こっちを実行
            #user = User.objects.create_user(username2, '', password2)
            print("except")
            return render(request,'mnist.html',{})
   

    #render:テンプレートhtmlの表示に使う
    #コンテキスト(第３引数):データの受け渡しに使う
    print("not")
    return render(request,'mnist.html',{'some':100})