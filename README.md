# Programming-Language
Python Based programming language, interpreted with python terminal.

[ How It Works ]
Programms will be created with a '.pl' file
The programming language will be interpreted with one python file

Lines can be assigned numbers with the '<' command file starts from line 0
e.g '<64'

The place in the order that the number is assigned to will be how the number is retrieved like a variable
a lines number can be read with the 'l' command
e.g. 'l1'

Assigned lines are like a stack, the order of assignment is how they should be retrieved
<6
<4
<3
So with the login in mind the order that the assigned numbers will be retrieved at is to get '6' you retrieve 0 to get 4 you retireve 1 ect.

A single number can be outputted with the '>' command
e.g. '>6'
This can be coupled with the 'r' command to output the retrieved number
e.g.
"  
<6 - line 0
>l0
"

Commands can be chained with the ':' command
e.g.
<33
>a:l0

A number can be converted to its corresponding ascii char wuth the 'a' command
>a33
This outputs a ! to the console


[ Example Code ]
>a33
<33
>a:l1
[ End of example code]
Line 0 Outputs ! to the console
Line 1 0 in the order is assigned 33
Line 2 Outputs the ascii code of placement 0 which is 33 so it outputs ! to the console
