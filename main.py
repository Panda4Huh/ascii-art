#   
#   * This file is a part of ascii-art
#   * main.py created by Igor Ordecha on 10/02/2020
#   * Copyright © 2020 . All rights reserved.
#   
#   ascii-art is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, version 3 of the License
#   
#   ascii-art is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   
#   You should have received a copy of the GNU General Public License
#   along with ascii-art.  If not, see <https://www.gnu.org/licenses/>.
#   
from PIL import Image, ImageEnhance
import argparse
if __name__ == "__main__":
	#czytanie argumentów
	parser = argparse.ArgumentParser(description='Generate ASCII art from images')
	parser.add_argument('path', metavar='PATH', type=str, help='a path to an image')
	parser.add_argument('--width', '-x', action='store', type=int, help='width of the output (DEFAULT: terminal width)')
	parser.add_argument('--height', '-y', action='store', type=int, help='height of the output (DEFUALT: correct aspect ratio from width)')
	parser.add_argument('--contrast', '-c', action='store', type=float, help='modify contrast (values >1 means more contrast, values <1 means less contrast, DEFAULT: 1)')
	args = parser.parse_args()
	
	#otwieranie pliku, manipulowanie nim
	img = Image.open(args.path).convert('LA')
	if args.width is not None and args.height is not None:
		img.thumbnail((args.width, args.height))
	if args.contrast is not None:
		img = ImageEnhance.Contrast(img).enhance(args.contrast)

	#tworzenie listy pixeli
	print(list(map(lambda tpl: tpl[0],list(img.getdata()))))

	img.show()

	#zamiana listy na ascii
	#	TBD

	#wyświetlanie i zapis do pliku
	#	TBD