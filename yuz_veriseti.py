import cv2
import os

kamera = cv2.VideoCapture(0)
kamera.set(3,640) #video genişliğini belirler.
kamera.set(4,480) #video yüksekliğini belirler.
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
imagePaths = [os.path.join("veriseti",f) for f in os.listdir("veriseti")]
id = []
for imagePath in imagePaths: 
    ids = int(os.path.split(imagePath)[-1].split(".")[0])
    if ids not in id:
        id.append(ids)
face_id = id[-1] + 1
MAXFOTOSAY = 50 #her bir yüz için kullanılacak imaj sayısı
name = input("Lütfen kullanıcın ismini ve soyismini yazınız (Örnek: Mehdi Koşaca):")
print("\n [INFO] Kayıtlar Başlıyor. Kameraya Bak ve Bekle...")

say = 0

while(True):
    ret, img = kamera.read()
    #img = cv2.flip (img, -1) # gerekiyorsa kullan
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    yuzler = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        say += 1
        #yakalanan imajı veriseti klasörüne kaydet.
        cv2.imwrite("veriseti/" + str(face_id) + '.' + str(say) + "." + str(name) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow("imaj", img)
        print("Kayıt no: ", say)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif say >= MAXFOTOSAY:
        break
#Belleği temizle
print("\n [INFO] Program Sonlanıyor ve Bellek Temizleniyor...")
kamera.release()
cv2.destroyAllWindows()
