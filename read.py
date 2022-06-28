import cv2 

'''
img=cv2.imread('Photos\cat.jpg') #read the photo
cv2.imshow('cat',img) #show the photo
cv2.waitKey(0) #wait time to show the photo 
'''

captura = cv2.VideoCapture('Videos\dog.mp4')
while (captura.isOpened()):
  ret, imagen = captura.read()
  print(imagen)
  if ret == True:
    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()