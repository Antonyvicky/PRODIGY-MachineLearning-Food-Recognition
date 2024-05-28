import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the calorie database with additional entries
calorie_database = {
    'apple': 237,
    'pizza': 285,
    'banana': 105,
    'cheeseburger': 303,
    'sushi': 200,
    'beetroot': 43,  # Calories per 100 grams
    'carrot': 41,    # Calories per 100 grams
    # Add more food items and their calorie information
}

# Function to get the food item name from the image filename
def get_food_item_from_filename(filename):
    # Assuming the filename format is like 'food_item.jpg' or 'food-item.png'
    food_item = os.path.splitext(filename)[0]  # Remove the file extension
    food_item = food_item.replace('-', '_').lower()  # Replace hyphens with underscores and convert to lower case
    return food_item

# Function to estimate calories based on food item name
def estimate_calories(food_item, calorie_database):
    return calorie_database.get(food_item, 'Calorie information not available')

# Function to display image with food item and calorie information
def display_image_with_info(img_path, food_item, calories):
    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.title(f'Food Item: {food_item.capitalize()}, Estimated Calories: {calories}')
    plt.axis('off')  # Hide axes
    plt.show()

# Process all images in a specified folder
def process_images_in_folder(folder_path, calorie_database):
    for img_name in os.listdir(folder_path):
        if img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, img_name)
            food_item = get_food_item_from_filename(img_name)
            calories = estimate_calories(food_item, calorie_database)
            display_image_with_info(img_path, food_item, calories)

# Example usage
folder_path = r'C:\\Users\\vigne\\OneDrive\\Desktop\\PRODIGY\\MACHINE LEARNING\\Task04\\images'
process_images_in_folder(folder_path, calorie_database)
