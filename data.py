from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from numpy import random
import numpy as np
import argparse

def create_image():
    	size = (72, 28)     #size of canvas
    	font = ImageFont.truetype('SignPainter.ttc', 28)

   	# create input image
    	input_img = Image.new("RGB", size, (0, 0, 0))
    	draw_input = ImageDraw.Draw(input_img)

    	# create label image
    	label_img = Image.new("RGB", size, (0, 0, 0))
    	draw_label = ImageDraw.Draw(label_img)
	
	# equation: "3 + 7"
	num1 = "1"
	op = "+"
	num2 = "7"
	
	#initialize index of image
	n = 1
	
	#check size of num1, num2, op
	#sizex1, sizey1 = font.getsize(num1)
	#sizeOp1, sizeOp2 = font.getsize(op)
	#sizex2, sizey2 = font.getsize(num2)
	#print sizex1, sizey1
	#print sizeOp1, sizeOp2
	#print sizex2, sizey2	
	
	# 1 example tets
	#x1 = 6
	#y1 = 2
	#xOp = 36
	#yOp = 8
	#x2 = 54
	#y2 = 2
	#draw_input.text((x1, y1), num1, (255, 255, 255), font=font)
	#draw_input.text((xOp, yOp), op, (255,255,255), font=font)
	#draw_input.text((x2, y2), num2, (255,255,255), font=font)
	
	#input_name = "input" + str(n) + ".png"	
	#input_img.save(input_name)
	#n += 1
							
	#rotate
	#current_image = Image.open(input_name)	
	#crop_num1 = current_image.crop((0,0,26,26)).rotate(-15)
    	#current_image.paste(crop_num1, (0,0))
	#current_image.save(input_name)										
	#crop_num2 = current_image.crop((50, 0, 72, 28)).rotate(60)
	#current_image.paste(crop_num2, (50,0))
	#current_image.save(input_name)
	
	n=1
	#loop over rotation: num1, num2 
	for x1 in np.arange(start=3, step=2, stop=6):
		for y1 in np.arange(start=2, step=2, stop=5):
			for xOp in np.arange(start=30, step=2, stop=37):
				for yOp in np.arange(start=1, step=2, stop=8):
					for x2 in np.arange(start=52, step=2, stop=55):
						for y2 in np.arange(start=2, step=2, stop=5):
							for r1 in np.arange(start=-15, step=8, stop=60):
								for r2 in np.arange(start=-15, step=8, stop=60):
									draw_input.text((x1, y1), num1, (255,255,255), font=font)
									draw_input.text((xOp, yOp), op, (255,255,255), font=font)
									draw_input.text((x2, y2), num2, (255,255,255), font=font)
									input_name = "input" + str(n) + ".png"	
									input_img.save(input_name)
									n += 1
							
									#rotate
									current_image = Image.open(input_name)	
									crop_num1 = current_image.crop((0,0,26,26)).rotate(r1)
    									current_image.paste(crop_num1, (0,0))
									current_image.save(input_name)										
									crop_num2 = current_image.crop((50, 0, 72, 28)).rotate(r2)
									current_image.paste(crop_num2, (50,0))
									current_image.save(input_name)
	
	#label
	#label_text = str(result)
	#label_text = "10"
    	#outText_x, outText_y = font1.getsize(label_text)
    	#x_label = (70 - outText_x)/2
    	#y_label = (28 - outText_y)/2
    	#draw_label.text((x_label, y_label), label_text, (0,0,0), font=font1)
	#label_name = "label" + str(i) + ".png"
	#label_img.save(label_name)
    
#create_image()
def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-n', '--num_samples', metavar='n', type=int, default=1, help='Number of sample')
	
	args = parser.parse_args()
	n = args.num_samples
	create_image()


if __name__ == '__main__':
	main()


