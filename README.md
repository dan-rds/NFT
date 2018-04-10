# NFT

A python script for quickly ceating a **N**ew **F**ile form a **T**emplate


### Installing
Simply clone this repository into a directory that you won't accidentally delete or move. I would recommend putting it in ~/ . Navigate to the newly created directory can run the following commands:


```
$ chmod a+x ./install
$ ./install
```
This will prompt you with a few commands to fill out the templates with your information. In order to source your bash profile, it'll ask you to login again. If this makes you uncomfortable, you can '^C' and run the source command manually with:
```
$ source ~/.bash_profile
```
### Running
Just like that, we should be in business. Now work something like the Touch command but instead of creating empty files, when Will create basic boilerplate files from the template. Try it out with something like:
```
$ nft test.java
```
Which created the folowing file:
```
/*-------------------------------------
test.java
project
    by Daniel Richards (ddrichar@ucsc.edu)
       on 4-9-2018
--------------------------------------*/

import java.util.*;
import java.lang.*;
import java.io.*;

public class test
{
        public static void main(String args[])
        {
                System.out.println("New Java file created from template")
        }
}
```
### Other File Types
NFT can also build non-source files. The standard README is included in the templates and he can be run with:
```
$ nft README
```
But the real coup de grace is the makefiles. NFT can build makefiles for Java and C projects and can even make a jar package. NFT will compile files beforehand to catch any nested classes that don't correspond .java files. Run the makefile script with:
```
$ nft Makefile
```

### Adding Templates
Also not as simple as the install, adding templates it's quite easy. In new_from_template.py you'll find a dictionary called file_types. Add an entry to the dictionary with the key (language name) and value (file extention). Next, in the ./templates sub-directory add a file named <key>.<value>. For instance if you wanted to add a C++ template, you could do something like:
```
file_types[C++]=cpp
```
Using the other templates as a reference, add specific replace wildcards for the program i.e. <date> <filename> <project>.

## Authors

* [**Daniel Richards**](https://danieldrichards.github.io/)


#### CAUTION
> As with any install from source, it is important to read it over and I understand what the code is doing.
Pay special attention bash scripts as well as any process calls in the Python scripts i.e. Popen, open, write or subproces. By design, this program will edit system files so if you don't understand what a command is doing, check the docs.   

## License

This project is unlicensed and in the [Public Domain](https://wiki.creativecommons.org/wiki/Public_domain) with the sole provision that if you make anything cool with my code, I want to know about it!

