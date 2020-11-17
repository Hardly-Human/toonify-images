import streamlit as st
from PIL import Image

def main():
  
	st.title("Toonify Images")
	st.text("Built with Toonify-API and Streamlit")
	st.markdown("### [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Hardly-Human/toonify-images)\
	`            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")

	image_file = st.file_uploader("Upload Image", type = ['jpg','png','jpeg'])

	if image_file is None:
		st.warning("Upload Image and Toonify")

	if image_file is not None:
		image1 = Image.open(image_file)
		rgb_im = image1.convert('RGB') 
		image = rgb_im.save("saved_image.jpg")
		image_path = "saved_image.jpg"
		st.image(image1)

	if st.button("Toonify 🎃 "):
		if image_file is not None:
			st.warning("Please wait.. by the way Nice picture..😊")
			r = requests.post(
			    "https://api.deepai.org/api/toonify",
			    files={
			        'image': open('saved_image.jpg', 'rb'),
			    },
			    headers={'api-key': 'aa48ee59-f392-4783-b1ac-ab410534ca61'}
			)

			color_image_url = r.json()["output_url"]

	else:
			st.error("Please Upload Image!!!")

if __name__== "__main__":
	main()