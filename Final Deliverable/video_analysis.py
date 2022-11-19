
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
import warnings
warnings.filterwarnings('ignore')
from tensorflow.keras.layers import MaxPooling2D
import cv2
import numpy as np
import keras
from keras.preprocessing import image
from keras.models import load_model
from twilio.rest import Client
from playsound import playsound
from tensorflow.keras.utils import load_img

model = load_model(r'forest1.h5')
video  = cv2.VideoCapture(0)
name = ['Forest','with fire']

account_sid = 'AC82143318302d2d70c5ae1a66e21f6755'
auth_token = '163eeb6a61129ca48d866590b8f7288c'
client = Client(account_sid , auth_token)
message = client.messages \
.create(
    body = 'Forest Fire is detected , stay alert',
    #use  twilo number
    from_ = '+19804468102',
    #to number
    to = '+916383239290'
)
print(message.sid)

from tensorflow.keras.utils import load_img
# from Sequential import predict_classes

while(1):
  success,frame = video.read()
  cv2.imread("/content/image.jpg",frame)
  img = image.load_img("/content/image.jpg",target_size=(64,64))
  x = image.img_to_array(img)
  x = np.expand_dims(x,axis = 0)
  pred = model.predict_classes(x)
  p = pred[0]
  print(pred)
  cv2.putText(frame , "predicted class =" +str(name[p]),(100,100),
              cv2.FONT_HERSHEY_SIMPLEX ,1,(0,0,0),1)