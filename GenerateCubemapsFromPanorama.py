import cv2
import numpy as np
import math

panorama = cv2.imread(r'\pano_000003_000436.jpg')

face_size = 1024  

directions = {
    "right": np.array([1, 0, 0]),
    "left": np.array([-1, 0, 0]),
    "top": np.array([0, 1, 0]),
    "bottom": np.array([0, -1, 0]),
    "front": np.array([0, 0, 1]),
    "back": np.array([0, 0, -1])
}

def direction_to_uv(direction, width, height):
    x, y, z = direction
    u = 0.5 + (np.arctan2(x, z) / (2 * np.pi))
    v = 0.5 - (np.arcsin(y) / np.pi)
    return int(u * width), int(v * height)

cubemap_faces = {}
for face_name, direction in directions.items():
    face = np.zeros((face_size, face_size, 3), dtype=np.uint8)
    for x in range(face_size):
        for y in range(face_size):
            # Map (x, y) on the cube face to a direction vector
            fx = (2 * (x / face_size) - 1)
            fy = (2 * (y / face_size) - 1)
            if face_name in ["top", "bottom"]:
                dz = 1.0
                if face_name == "top":
                    direction_vector = np.array([fx, dz, fy])
                else:
                    direction_vector = np.array([fx, -dz, fy])
            else:
                dz = 1.0
                if face_name == "back":
                    direction_vector = np.array([fx, fy, dz])
                elif face_name == "front":
                    direction_vector = np.array([-fx, fy, -dz])
                elif face_name == "left":
                    direction_vector = np.array([dz, fy, -fx])
                elif face_name == "right":
                    direction_vector = np.array([-dz, fy, fx])
            direction_vector = direction_vector / np.linalg.norm(direction_vector)

            u, v = direction_to_uv(direction_vector, panorama.shape[1], panorama.shape[0])

            face[y, x] = panorama[v % panorama.shape[0], u % panorama.shape[1]]

    cubemap_faces[face_name] = face

for face_name, face_img in cubemap_faces.items():
    flipped_horizontally = cv2.flip(face_img, 1)
    if str(face_name) != 'bottom' and str(face_name) != 'top':
        flipped_horizontally = cv2.rotate(flipped_horizontally, cv2.ROTATE_90_CLOCKWISE)
        flipped_horizontally = cv2.rotate(flipped_horizontally, cv2.ROTATE_90_CLOCKWISE)
    if face_name == 'top':
        flipped_horizontally = cv2.rotate(flipped_horizontally, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(rf'{face_name}.jpg', flipped_horizontally)
