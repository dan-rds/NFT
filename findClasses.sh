#!/bin/bash
if[$1 -eq '-jar']; then
	echo "JAR"
fi
javac *.java 

classes=`ls *.class`

for cl in $classes; do
	echo $cl
done
rm -f *.class
exit