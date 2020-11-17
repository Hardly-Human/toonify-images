import streamlit as st
from PIL import Image
import requests
import base64
import os

def footer():
	st.markdown("""
	* * *
	Built with ❤️ by [Rehan uddin](https://hardly-human.github.io/)
	""")
	st.success("Rehan uddin (Hardly-Human)👋😉")
	st.markdown("### [Give Feedback](https://www.iamrehan.me/forms/feedback_form/feedback_form.html)\
	 `            `[Report an Issue](https://www.iamrehan.me/forms/report_issue/report_issue.html)")



def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">[ Download Image ]</a>'
    return href

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

			img_data = requests.get(color_image_url).content
			with open('toonified_image.jpg', 'wb') as handler:
				handler.write(img_data)
			st.success("That looks good..🎊✨")
			toonified_image = Image.open('toonified_image.jpg')

			st.subheader("Toonified Image")
			st.image(toonified_image)

			st.markdown(get_binary_file_downloader_html('toonified_image.jpg', 'Picture'), unsafe_allow_html=True)

		else:
			st.error("Please Upload Image!!!")

if __name__== "__main__":
	main()
	footer()