from PIL import Image
import os

def create_patterned_image(input_path, output_path, repetitions):
    try:
        img - Image.open(input_path)
        img_width, img_height = img.size

        #create a new image with the specified pattern layout
        pattern_width = img_width * repetitions
        pattern_height = img_height* repetitions
        pattern_img = Image.new('RGB', (pattern_width, pattern_height))
    
        for i in range(repetitions):
            for j in range(repetitions):
                pattern_img.paste(img, (i* img_width, j* img_height))

        pattern_img.save(output_path, quality =95)
        print(f"patterned image saved at {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    repetitions = 3
    if not os.path.exists(output_folder):
        os.mkdirs(output_folder)
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        create_patterned_image(input_path, output_path, repetitions)
        

