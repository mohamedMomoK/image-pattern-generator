from PIL import Image
import os
import sys

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
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except OSError:
        print(f"Invalid image format: {input_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) <4:
        print("usage: python main.py <input_folder> <output_folder> <repetitions>")
        sys.exit(1)
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    repetitions = int(sys.argv[3])

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        create_patterned_image(input_path, output_path, repetitions)


