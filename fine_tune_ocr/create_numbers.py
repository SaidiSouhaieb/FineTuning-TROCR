import os
import cv2

# Function to load images from a folder


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

# Function to create a new folder


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to combine two images horizontally


def combine_images_horizontally(img1, img2):
    distance = 30
    # Calculate the new widths for img1 and img2 after removing distance
    new_width_img1 = img1.shape[1] - distance // 2
    new_width_img2 = img2.shape[1] - distance // 2

    # Resize img1 and img2
    img1_resized = cv2.resize(img1, (new_width_img1, img1.shape[0]))
    img2_resized = cv2.resize(img2, (new_width_img2, img2.shape[0]))

    # Combine resized img1 and img2
    combined_image = cv2.hconcat([img1_resized, img2_resized])

    return combined_image

# Function to save combined image


def save_combined_image(combined_img, folder_name, index):
    output_path = os.path.join(folder_name, f"{index}.png")
    cv2.imwrite(output_path, combined_img)

# Main function


def main():
    source_folder = "data"
    destination_folder = "data"
    create_folder(destination_folder)
    first_number_list = [1]
    second_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in second_number_list:
        # Load images from source folders
        folder1 = os.path.join(source_folder, str(1))
        images1 = load_images_from_folder(folder1)

        folder2 = os.path.join(source_folder, str(i))
        images2 = load_images_from_folder(folder2)

        # Combine images and save
        min_len = min(len(images1), len(images2))
        for j in range(min_len):
            print(destination_folder + "/" + str(i))
            combined_img = combine_images_horizontally(images1[j], images2[j])
            save_combined_image(
                combined_img, destination_folder + "/" + "1" + str(i), i * 10 + j)


if __name__ == "__main__":
    main()
