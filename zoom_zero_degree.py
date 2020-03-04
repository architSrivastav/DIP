'''
    Replication for Image scaling
    
    Submitted by: 
    Archit Srivastava 18ucs054
    Shubham Chokhani  18ucs136
    To: 
    Dr. Anukriti Bansal

    This program uses zero order hold also called pixel replication or nearest neighbour
    interpolation technique to give a zoomed effect to the image
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
                a   b           a   a   b   b
                        -->     a   a   b   b                
                c   d           c   c   d   d
                                c   c   d   d
        '''
        for row in range(y, y+100, 2):
            for col in range (x, x+100, 2):
                #condition to check that we dont go out of bounds
                if((row+1) < (w-1) and (col+1) < (h-1) and (row-j) < (w-1) and (col-i) < (h-1) ):
                    #doing pixel replication:
                    result[int(row),col] =  image[int(row-j), int(col-i)]
                    result[int(row+1),col] =  image[int(row-j), int(col-i)]
                    result[row,int(col+1)] = image[int(row-j), int(col-i)]
                    result[int(row+1), int(col+1)] = image[int(row-j), int(col-i)]
                    i  += 1
            j  += 1
            #reset i for nest iteration
            i = 0
                
        #assign the new pixel values in original image to display it
        image[y:y+100, x:x+100] = result[y:y+100, x:x+100]
        #draw a rectangle highlighting the zoomed area
        cv2.rectangle(image, (x,y), (x+100, y+100), (255,0 ,255), 1)
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

