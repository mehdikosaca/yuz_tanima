## YÜZ TANIMA SİSTEMİ
Bu repo oluşturacağınız yüz verisetlerini tanımaya çalışan makine öğrenmesi temelli bir python yazılımıdır. 

### Program Hakkında
Programı maksimum verimle kullanmak için kaliteli bir kamera kullanın. Kamera başlatıldıktan sonra kameraya bakarak sabit durun. Hareket ederek alınan anlıklar programın performansını düşürmektedir. 

#### Sistem Bağımlılıkları
* Python3
#### Python Bağımlılıkları
* opencv
* Pillow
* numpy
* os

### Kullanımı
#### Repoyu klonla
```
git clone https://github.com/mehdikosaca/yuz_tanima.git
```
```
cd yuz_tanima
```
#### Veriseti oluşturmak için
```
python yuz_veriseti.py
```
kodunu çalıştırdıktan sonra kullanıcının ismini ve soyismini yazınız. Alınan anlıklar veriseti klasörüne kaydedilecektir. Lütfen bu klasöre dosya eklemeyiniz veya silmeyiniz.

#### Verisetini eğitmek için
Oluşturduğunuz verisetini aşağıdaki komutla eğitebilirsiniz. Verisetine her veri eklendiğinde tekrar eğitim yapmayı unutmayınız.
```
python yuz_egitimi.py
```

#### Yüz tanımak için
Eğitilmiş veri kümesini kullanarak yüz tanıma işlemi yaptırmak için aşağıdaki komutu çalıştırınız.
```
python yuz_tanima.py
```

### Referanslar
Bu repo https://python.gurmezin.com/python-ve-opencv-ile-yuz-tanima/ sitesindeki kodların güncellenmiş versiyonudur. Paket haline getirilmesi için de değişiklikler yapılmıştır. 

### İletişim
Programı çalıştırırken bir bugla karşılaştıysanız ya da sormak istediğiniz sorular varsa lütfen benimle iletişime geçin.
* mehdi.kosaca@msfr.ibg.edu.tr 
