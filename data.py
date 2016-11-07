from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from numpy import random
import argparse

def create_image(n):
	for i in range (1, n+1):
    		size = (72, 28)     #size of canvas
    		font = ImageFont.truetype('Arial.ttf', 14)

    		# input image
    		input_img = Image.new("RGB", size, (255, 255, 255))
    		draw_input = ImageDraw.Draw(input_img)

    		#label image
    		label_img = Image.new("RGB", size, (255, 255, 255))
    		draw_label = ImageDraw.Draw(label_img)

    		# get random numbers
    		num1 = random.randint(0, 10)
    		num2 = random.randint(0, 10)

    		# get random operator (+/-)
    		op = random.randint(0, 2)
    		if op==0:
        		operator = "+"
        		result = num1 + num2
    		else:
        		operator = "-"
        		result = num1 - num2
 
	    	# number1, number2, opertor sizes
		inText_x, inText_y = font.getsize(str(num1))
		opText_x, opText_y = font.getsize(operator)
		
		#num1 image
		num1_x = random.randint(0,20)
		num1_y = random.randint(0, 14)
		num2_x = random.randint(49, 65)
		num2_y = random.randint(0,14)
		op_x = random.randint(27, 43)
		op_y = random.randint(0, 14) 
		#draw_input.text((num1_x, num1_y), str(num1), (0,0,0),font=font)
		draw_input.text((num1_x, num1_y), "3", (0,0,0), font=font)
		#draw_input.text((op_x, op_y), operator, (0,0,0), font=font)
		draw_input.text((op_x, op_y), "+", (0,0,0), font=font)
		#draw_input.text((num2_x, num2_y), str(num2), (0,0,0), font=font)
		draw_input.text((num2_x, num2_y), "7", (0,0,0), font=font)
	
    		#label
    		#label_text = str(result)
		label_text = "10"
    		outText_x, outText_y = font.getsize(label_text)
    		x_label = (70 - outText_x)/2
    		y_label = (28 - outText_y)/2
    		draw_label.text((x_label, y_label), label_text, (0,0,0), font=font)
		input_name = "input" + str(i) + ".png"    		
		input_img.save(input_name)
		#label_name = "label" + str(i) + ".png"

		#label_img.save(label_name)
    

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-n', '--num_samples', metavar='n', type=int, default=1, help='Number of sample')
	
	args = parser.parse_args()
	n = args.num_samples
	create_image(n)


if __name__ == '__main__':
	main()


