from ultralytics import YOLO
import cv2

def blur_children_faces(image_name):
    model = YOLO('best.pt')
    image = cv2.imread(f'uploaded/{image_name}')

    if image is None:
        raise ValueError("Image not found or path is incorrect")

    results = model(image)
    
    for result in results[0].boxes:  
        x_min, y_min, x_max, y_max = map(int, result.xyxy[0])  
        roi = image[y_min:y_max, x_min:x_max]
        blurred_roi = cv2.GaussianBlur(roi, (101, 101), 0)
        image[y_min:y_max, x_min:x_max] = blurred_roi

    cv2.imwrite(f'static/results/{image_name}', image)

    return {
        "resultPath": f'static/results/{image_name}'
    }

