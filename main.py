from PIL import Image, ImageDraw

# Create an image with a white background
width, height = 500, 500
image = Image.new('RGB', (width, height), 'white')

# Draw on the image
draw = ImageDraw.Draw(image)

# Draw the monkey's face
face_x, face_y, face_radius = width // 2, height // 2, 150
draw.ellipse((face_x - face_radius, face_y - face_radius, face_x + face_radius, face_y + face_radius), fill='saddlebrown', outline='black', width=3)

# Draw the monkey's ears
ear_radius = 50
draw.ellipse((face_x - face_radius - ear_radius, face_y - ear_radius, face_x - face_radius + ear_radius, face_y + ear_radius), fill='saddlebrown', outline='black', width=3)
draw.ellipse((face_x + face_radius - ear_radius, face_y - ear_radius, face_x + face_radius + ear_radius, face_y + ear_radius), fill='saddlebrown', outline='black', width=3)

# Draw the monkey's eyes
eye_radius = 20
eye_x_offset = 50
eye_y_offset = 30
draw.ellipse((face_x - eye_x_offset - eye_radius, face_y - eye_y_offset - eye_radius, face_x - eye_x_offset + eye_radius, face_y - eye_y_offset + eye_radius), fill='white', outline='black', width=3)
draw.ellipse((face_x + eye_x_offset - eye_radius, face_y - eye_y_offset - eye_radius, face_x + eye_x_offset + eye_radius, face_y - eye_y_offset + eye_radius), fill='white', outline='black', width=3)

# Draw the monkey's pupils
pupil_radius = 10
draw.ellipse((face_x - eye_x_offset - pupil_radius, face_y - eye_y_offset - pupil_radius, face_x - eye_x_offset + pupil_radius, face_y - eye_y_offset + pupil_radius), fill='black')
draw.ellipse((face_x + eye_x_offset - pupil_radius, face_y - eye_y_offset - pupil_radius, face_x + eye_x_offset + pupil_radius, face_y - eye_y_offset + pupil_radius), fill='black')

# Draw the monkey's mouth
mouth_x_offset = 50
mouth_y_offset = 80
draw.arc((face_x - mouth_x_offset, face_y + mouth_y_offset - 20, face_x + mouth_x_offset, face_y + mouth_y_offset + 20), start=0, end=180, fill='black', width=3)

# Display the image
image.show()