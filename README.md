# Image Generator  
This console application is intended for PNG image generation
based on Excel spreadsheet.  
For each cell, except those contained in the zero columns 
and rows, an image is created with transliterated text 
from this cell.
For each column a folder is created with the name from the 
zero row. File name for each image matches to text in zero
column of corresponding row. Files, which created for each
column, are placed in the folder of matched column. Aligning 
text in an image - centered.

## Application work example
![Initial table](/examples/test_table.png "Initial table")  
![Result](/examples/result_1.png "Result")  
![](/examples/result_2.png)

## Installation
_It is assumed that you have installed `Python` and the 
package manager` pip`._

Install necessary dependencies:  
```shell
pip install requirements.txt
```

## Command line parameters  
_All parameters are optional. You can specify parameters in 
any order._
* ___Help -h, --help___  
Brief parameters description. 
* ___Path to table -n, --name___  
Specify the path to the table with which you plan to work.
The default spreadsheet is `test_table.xlsx` from this 
repository.
* ___Sheet -sh, --sheet___  
Specify the number of the required sheet (starting from 0) or
its title.
* ___Font -f, --font___  
Specify the path to the font file. In Windows 10, it is enough 
to specify name (for preinstalled fonts). Times New Roman is
used by default.
* ___Background colour -b, --back___  
Specify background colour in `RGB` or `hex`. White is used by
default.
* ___Text colour -t, --text___  
Specify background colour in `RGB` or `hex`. Black is used by
default.
* ___Text size -s, --size___  
Enter integer number, 80 by default.
* ___Width padding -w, --wpad___  
Enter integer number, 20 by default.
* ___Height indent -hp, --hpad___  
Enter integer number, 10 by default.
* ___Path to the folder -p, --path___  
Specify path to the folder in which you want to save the 
result of application work. If the specified folder exists, 
the files will be written to it. By default `images` is 
created.  

___Example of using parameters:___
```shell
main_file.py -n new_table.xlsx -sh 0 -f BOOKOS.TTF -b '#d5b59c' -t rgb'(13, 33, 79)' -s 90 -w 30 -hp 20 -p 'new_example'
```
