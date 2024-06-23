# marfhingpl interpreted edition

![mammas evo - copian5](https://github.com/dygkkh/marfhingpl/assets/158525086/0b1f05f8-8871-4c87-98b7-7527f72ecbd4)

marfhing programming language last beta edition


marfhing is a mini proyect of a programming language similar to assembly, easiest and with less freatures
because language is in 0.1 beta.
this language is interpreted, but i´m working in the compiled version. 
this language is a assembler but easiest and less freatures
because language is in 0.1 beta, I will update the language


how to download/install
-

first you need to download from this repository one of this versions. the file is a *.zip. 
second you need to extract the files of the *.zip.
the last step of the instalation is that you need to move that files to C:\Windows\System32 (I know that you distrust me)

i´m working to only need to add the direction of that programs to path.


to do a print you need to do this:


![imprint](https://github.com/dygkkh/marfhingpl/assets/158525086/d10d206a-553a-4d45-9bc7-073ac863a304)

with a function named "imprint" you print in screen a text
with "endtok;", you finish the tokenizer

you can put numbers in a global list and do operations with him with the function "put"

for example:

input:


put 1
put 1
endtok;


output:

&: program_started

&: end_program

and you can sum all values of the global list using "sum":
example:
#input:


put 1
put 1
sum
endtok;


output:

&: program_started

&: end_program


the "sum" function sum all the values of the global list, but we didn´t show the value. to show the value, you need to use the function "val.show;"
example:
#input:


put 1
put 1
sum
val.show;
endtok;

output:
&: program_started

1

&: end_program

if you want to do with a input in the shell, yo need to use the function "addtok_intinput;" in the place of the "put" function.


thanks to @basvdl97 to help me so much in the proyect with his videos on youtube

report errors to solve in issues
