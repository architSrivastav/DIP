''' Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
    This program does shrinking by deleteing alternate rows and columns to 
    give a zoom out effect to the image. This method is corresponding to 
    "replication" method used for image scaling.
    Usage: 
    requires lena_color.tif in the directory to function
    on left mouse click it displays a box within the image that shows zoomed
    effect on pixels in vicinity of the mouse click.
    press 'c' to exit
    press 'r' to reset image back to normal
'''


import cv2


def mouseHandler(event, x, y, flags, params):
    #when mouse left button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:   
        #create a copy of original image
        result = image.copy() 
        #height h and width w of image so that we don't go out of bounds while computation
        h, w = result.shape[0:2]
        #initialised before loop
        i = 0
        j = 0
        #main algo:
        '''
                a   b   c           a   c
                e   f   g   -->     
                i   j   k           i   k
        '''
        for row in range(y, y+50):
            for col in range (x, x+50):
                #condition to check that we dont go out of bounds
                if((row + j) < (w-1) and (col+i) < (h-1)):
                    #doing shrinking:
                    result[row,col] =  image[int(row + j), int(col+i)]
                    result[int(row+1),col] =  image[int(row+j), int(col+i)]
                    result[row,int(col+1)] = image[int(row+j), int(col+i)]
                    result[int(row+1), int(col+1)] = image[int(row+j), int(col+i)]
                    i  += 1
            j  += 1
            #reset i for next iteration
            i = 0
                
        #assign the new pixel values in original image to display it
        image[y:y+50, x:x+50] = result[y:y+50, x:x+50]
        #draw a rectangle highlighting the zoomed area
        cv2.rectangle(image, (x,y), (x+50, y+50), (255,0 ,255), 1)
        #display image
        cv2.imshow("image", image)
        
#read image in grayscale
image = cv2.imread("lena_color.tif")
#clone the image to use it for resetting the image back to normal
clone = image.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouseHandler)

# keep looping until the 'c' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
 
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
