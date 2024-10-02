import streamlit as st


# 1. Displaying Text
st.write("Welcome to My First Streamlit App!")

# 2. Adding a Header
st.header("This is a Header")

# 3. Using a Button
if st.button("Click Me!"):
    st.write("Button Clicked!")

# 4. Displaying a Simple List
fruits = ["Apple", "Banana", "Cherry"]
st.write(fruits)

#5. display image from URL
def display_image_from_url(url):

    st.image(url, caption='Image from URL', width=300)

if __name__ == '__main__':
  # Replace 'https://example.com/image.jpg' with the actual URL of your image
  image_url = 'https://cdn-images-1.medium.com/max/1600/1*Hu4TWEt6o3iAWeqxqklbZg.jpeg'
  display_image_from_url(image_url)