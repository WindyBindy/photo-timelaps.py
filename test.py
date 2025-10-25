# # import pygame
# # import pygame.camera
# # import cv2


# # # Initialize camera module
# # pygame.camera.init()
# # # Get list of available cameras
# # cams = pygame.camera.list_cameras()
# # print(cams)
# # if cams:
# #     cam = pygame.camera.Camera(cams[2], (1000, 1000), "RGB")
# #     cam.start()
# #     img = cam.get_image()
# #     pygame.image.save(img, "capture.jpg")
# #     cam.stop()
# # else:
# #     print("No camera found.")


# import cv2
# import pygame

# nameOfTheFile = "1.jpg"
# WIDTH = 1280
# HEIGHT = 720
# # Initialize pygame window (optional if just saving image)
# pygame.init()

# # Open camera
# cap = cv2.VideoCapture(2)  # 0 = first camera

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# cap.set(3, WIDTH)
# cap.set(4, HEIGHT)
# # Read one frame
# ret, frame = cap.read()
# cap.release()

# # frame is in BGR -> Convert to RGB (correct colors)
# frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# # Convert to pygame surface (if needed)
# pygame_image = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))

# # Save normal image
# cv2.imwrite(nameOfTheFile, frame)  # Saves correctly colored image

# print("done photo")
import datetime

x = datetime.datetime.now()
print(x)
