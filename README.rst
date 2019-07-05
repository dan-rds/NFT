===
NFT
===

A python script for quickly ceating a **N**\ ew **F**\ ile form a
**T**\ emplate

Installing
~~~~~~~~~~

::

    $ pip install nft


Running
~~~~~~~

Just like that, we should be in business. NFT works something like the touch command but instead of creating empty files, nft creates
boilerplate files from the template. The first time you run nft, it will ask a few questions to better fill out the template. Try it out with something
like:

::

    $ nft test.java

Which created the following file:

::

    /*-------------------------------------
    test.java
    temp_project
        by Daniel Richards (ddrichar@ucsc.edu)
           on 4-9-2019
    --------------------------------------*/

    import java.util.*;
    import java.lang.*;
    import java.io.*;

    public class test
    {
            public static void main(String args[])
            {
                    System.out.println("New Java file created from template");
            }
    }

Other File Types
~~~~~~~~~~~~~~~~
NFT can make the following kinds of source files:
- C files and headers
- Java
- Python
- Ruby
- Shell (bash and Csh)

NFT can also build non-source files. The standard README types are included:
- README (txt)
- README.md (markdown)
- README.rst (restructured text)

Any of these can be run as follows:

::

    $ nft README.md

NOTE
~~~~
If you want to reenter your name or email or recompile the list of templates (if you added a new template) use:

::

    $ nft setup

Authors
-------

-  `Daniel Richards <https://github.com/dan-rds>`__

License
-------

See ./LICENSE 