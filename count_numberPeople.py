import cv2

# path_to_video="data\\openCV\\dataset.mp4"
path_to_video="D:\AI\CV\Background_subtraction\code_togit\data\openCV\\VTest.avi"
fgbg = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture(path_to_video)


# frame_width = int(capture.get(4))
# frame_height = int(capture.get(5))
# # out = cv2.VideoWriter("frame_result_output.mp4", cv2.VideoWriter_fourcc('M','J','P','G'),30, (frame_width,frame_height))

line = 280


contours_previous  = []
people_out = 0
people_in = 0
contours_now  = []

while True:
    
    contours_now  = []
    (grabbed, frame) = capture.read()
  
    if not grabbed:
        break
   
    fgMask = fgbg.apply(frame)
    
    cv2.putText(frame, str(capture.get(cv2.CAP_PROP_POS_FRAMES)) + "/433", (15, 15),
               cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (255,0,0))
    
    fgMask = cv2.threshold(fgMask, 200, 255, cv2.THRESH_BINARY)[1]

    fgMask = cv2.dilate(fgMask, None, iterations=2)
    fgMask = cv2.erode(fgMask, None, iterations=2)
    
    contours_list, hierarchy = cv2.findContours(fgMask,
                                       cv2.RETR_TREE ,
                                       cv2.CHAIN_APPROX_SIMPLE) # Find contours
    for c in contours_list:
        if cv2.contourArea(c) < 1000:
            continue
            
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0,255,0), 2)
        contours_now.append([x,y])
    
    # if len(contours_previous) == 0:
    #     contours_previous = contours_now
    #     continue
        
    # closest_contour_list = []
    

    # for i in range (len(contours_now)):
    #     minimum = 1000000
    #     closest_contour = -1
    #     for k in range(len(contours_previous)):
    #         diff_x = contours_now[i][0] - contours_previous[k][0]
    #         diff_y = contours_now[i][1] - contours_previous[k][1]
                        
    #         distance = diff_x**2 + diff_y**2
    #         if(distance < minimum and distance < 50):
    #             minimum = distance
    #             closest_contour = k
                        
    #     closest_contour_list.append(closest_contour)
                        
    # for i in range (len(contours_now)):

    #     if (closest_contour_list[i] >= 0):
    #         y_previous = contours_previous[closest_contour_list[i]][1]
    #         if (contours_now[i][1] < line and y_previous >= line):
    #             people_out = people_out + 1

    #         if (contours_now[i][1] >= line and y_previous < line):
    #             people_in = people_in + 1
        
    # contours_previous = contours_now
    
                        
    # cv2.line(frame, (0,line), (frame.shape[1], line), (0,255,255), 2)
    # cv2.putText(frame,"People out: " +str(people_out), (15,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    # cv2.putText(frame,"People in: " +str(people_in), (14,80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255),2 )

    #show the current frame and the fg masks
    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)
    ## [show]

    keyboard = cv2.waitKey(1) & 0xFF;
    if keyboard == 'q' or keyboard == 27:
        break
        
capture.release()
cv2.destroyAllWindows()