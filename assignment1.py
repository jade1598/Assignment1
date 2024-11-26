import cv2
import time

#----------------------------------------------------------------------------
# 1
cap = cv2.VideoCapture(0) #initialize video capture
while True:
    ret, frame = cap.read()  #read images
    if not ret:
        print("Failed to capture frame. Exiting.")
        break
    cv2.imshow('Webcam Feed', frame)  #display

    #stop if "ESC" is pressed
    if cv2.waitKey(1) & 0xFF == 27: 
        break

cap.release()
cv2.destroyAllWindows()

#----------------------------------------------------------------------------
#2

cap = cv2.VideoCapture(0)  
frame_times = []  #list to store the processing times for each frame

while True:
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting.")
        break

    #calculate FPS
    end_time = time.time()  #record the end time
    frame_time = end_time - start_time  #calculate the processing time
    frame_times.append(frame_time)  #save the processing time in the list

    fps = 1 / frame_time if frame_time > 0 else 0  #calculate FPS

    #display FPS on the frame
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

 
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release() 
cv2.destroyAllWindows() 

#calculate the average processing tme and FPS
if frame_times:
    average_time = sum(frame_times) / len(frame_times)  
    print(f"Average time per frame: {average_time:.4f} seconds")
    print(f"Average FPS: {1 / average_time:.2f}")
 
#----------------------------------------------------------------------------
#3
cap = cv2.VideoCapture(0)  
frame_times = []  

while True:
    start_time = time.time()

    ret, frame = cap.read()  
    if not ret:
        break

    #convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #find the brightest spot
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)

    #mark it on the frame
    cv2.circle(frame, max_loc, 10, (0, 0, 255), 2)

    #FPS
    end_time = time.time()
    frame_time = end_time - start_time
    frame_times.append(frame_time)  

    fps = 1 / frame_time if frame_time > 0 else 0 

    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow('Brightest Spot Detection', frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release() 
cv2.destroyAllWindows() 

if frame_times:
    average_time = sum(frame_times) / len(frame_times)  
    print(f"Average time per frame: {average_time:.4f} seconds")
    print(f"Average FPS: {1 / average_time:.2f}")

#3bis - whitout displaying the image

cap = cv2.VideoCapture(0)  
frame_times = []  

start_program = time.time() 

while True:
    current_time = time.time()  
    elapsed_time = current_time - start_program  

    if elapsed_time > 3:  # stop the loop after 3 seconds
        break

    start_time = time.time()  

    ret, frame = cap.read()  
    if not ret:
        break

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
   
    end_time = time.time()  
    frame_time = end_time - start_time  
    frame_times.append(frame_time)  

    fps = 1 / frame_time if frame_time > 0 else 0  

cap.release()  
cv2.destroyAllWindows()  

if frame_times:
    average_time = sum(frame_times) / len(frame_times)  
    print(f"Average time per frame: {average_time:.4f} seconds")
    print(f"Average FPS without display: {1 / average_time:.2f}")

#----------------------------------------------------------------------------
#4

cap = cv2.VideoCapture(0) 

while True:
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    #extract red channel
    red_channel = frame[:, :, 2]

    # find the reddest spot
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(red_channel)

    #mark the reddest spot
    cv2.circle(frame, max_loc, 10, (255, 0, 0), 2)

    end_time = time.time()
    fps = 1 / (end_time - start_time)

    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Reddest Spot Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

#----------------------------------------------------------------------------
#5

cap = cv2.VideoCapture(0)  
frame_times = []  

while True:
    start_time = time.time()  
    ret, frame = cap.read()  
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # find the brightest spot manually 
    brightest_val = 0  # maximum brightness value
    brightest_loc = (0, 0)  #coordinates of the brightest pixel

    # apply the double loop through all pixels in the grayscale image
    for y in range(gray.shape[0]):  # through each row of the image
        for x in range(gray.shape[1]):  # through each column of the image
            if gray[y, x] > brightest_val:  # compare current pixel's brightness
                brightest_val = gray[y, x]  # update the maximum brightness value
                brightest_loc = (x, y)  # update the coordinates of the brightest pixel

    # mark the brightest spot on the original frame
    cv2.circle(frame, brightest_loc, 10, (0, 255, 255), 2)

    #FPS
    end_time = time.time()  
    frame_time = end_time - start_time 
    frame_times.append(frame_time)  

    fps = 1 / frame_time if frame_time > 0 else 0  

    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Brightest Spot with Loops', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key code is 27
        break

cap.release() 
cv2.destroyAllWindows()  

if frame_times:
    average_time = sum(frame_times) / len(frame_times)  
    print(f"Average time per frame: {average_time:.4f} seconds")
    print(f"Average FPS using loops: {1 / average_time:.2f}")


#----------------------------------------------------------------------------
#6

cap = cv2.VideoCapture(0)  
latencies = []  #list to store latencies for each frame

while True:
    capture_start = time.time()  #record the time before capturing the frame

    ret, frame = cap.read()
    if not ret:
        break

    # get the current time when the frame is captured
    capture_time = time.time()

    # calculate the latency (time between capture and now)
    display_time = time.time()
    latency = display_time - capture_start  
    latencies.append(latency)  

    # display latency on the frame
    latency_text = f"Latency: {latency * 1000:.2f} ms"
    cv2.putText(frame, latency_text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Latency Measurement", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# calculate and print the average latency
if latencies:
    average_latency = sum(latencies) / len(latencies)
    print(f"Average latency: {average_latency * 1000:.2f} ms")