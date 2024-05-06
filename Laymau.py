import cv2
import sqlite3
cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# insert/update data to sqlite
def insertOrUpdate(Ids, Tens):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE Id = " + str(Ids)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        conn.execute("UPDATE People SET Name = ? WHERE Id = ? ", (Tens, Ids))
    else:
        conn.execute("INSERT INTO People(Id, Name) Values(?, ?)", (Ids, Tens))
    conn.commit()
    conn.close()
idt = input("enter your id ")
tent = input("enter your name ")
insertOrUpdate(idt, tent) 
sampleNum = 0
while (True):
    # camera read
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
         # incrementing sample number
         sampleNum = sampleNum + 1
         # saving the captured face in the dataset folder
         cv2.imwrite("Anh/user." + idt + "." + str(sampleNum) + ".jpg", gray[y:y + h,x:x + w])
         cv2.imshow('frame', img)
    # wait for 100 mili seconds

    if cv2.waitKey(100) & 0xFF == ord('q'):
       break
    # break if the sample number is more than 20
    elif sampleNum > 20:
       break
cam.release()
cv2.destroyAllWindows()
