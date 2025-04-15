def cubemap_to_equirectangular(cubemap_faces, width, height):
    equirectangular = np.zeros((height, width, 3), dtype=np.uint8)

    for x in range(width):
        for y in range(height):
            theta = (x / width) * 2 * np.pi - math.radians(90) # azimuth
            phi = (y / height) * np.pi        # elevation

            x_dir = np.sin(phi) * np.cos(theta)
            y_dir = np.cos(phi)
            z_dir = np.sin(phi) * np.sin(theta)

            if abs(x_dir) >= abs(y_dir) and abs(x_dir) >= abs(z_dir):
                if x_dir > 0:
                    face = 4  # +X -> right
                    u = -z_dir / x_dir
                    v = -y_dir / x_dir
                else:
                    face = 3  # -X -> left
                    u = z_dir / -x_dir
                    v = -y_dir / -x_dir
            elif abs(y_dir) >= abs(x_dir) and abs(y_dir) >= abs(z_dir):
                if y_dir > 0:
                    face = 1  # +Y -> top
                    u = x_dir / y_dir
                    v = z_dir / y_dir
                else:
                    face = 2  # -Y -> bottom
                    u = x_dir / -y_dir
                    v = -z_dir / -y_dir
            else:
                if z_dir > 0:
                    face = 0  # +Z -> front
                    u = x_dir / z_dir
                    v = -y_dir / z_dir
                else:
                    face = 5  # -Z -> back
                    u = -x_dir / -z_dir
                    v = -y_dir / -z_dir

            u = (u + 1) / 2
            v = (v + 1) / 2

            if 0 <= u < 1 and 0 <= v < 1:
                u_index = int(u * cubemap_faces[face].shape[1])
                v_index = int(v * cubemap_faces[face].shape[0])
                equirectangular[y, x] = cubemap_faces[face][v_index, u_index]

    return equirectangular

# Load the cubemap images (6 faces)
cubemap_faces = [
    cv2.imread(r' front.jpg'),   # +Z
    cv2.imread(r' top.jpg'),     # +Y
    cv2.imread(r' bottom.jpg'),  # -Y
    cv2.imread(r' left.jpg'),    # -X
    cv2.imread(r' right.jpg'),   # +X
    cv2.imread(r' back.jpg')     # -Z
]

# Specify the width and height of the equirectangular image
equirect_width = 5000
equirect_height = 2700

equirect_image = cubemap_to_equirectangular(cubemap_faces, equirect_width, equirect_height)
equirect_image = cv2.flip(equirect_image, 1)


cv2.imwrite(r'equirectangular_image.jpg', equirect_image)
