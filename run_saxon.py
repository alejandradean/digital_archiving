import subprocess

subprocess.call(['java', '-jar', 'C:\\Program Files\\saxon9he.jar', '-s:C:\\Users\\adean\\Desktop\\converted.xml', '-xsl:C:\\Users\\adean\\Desktop\\hs6_07_1411.xsl', '-o:C:\\Users\\adean\\Desktop\\metadata\\output.xml'], shell=True)
# temp use of \\ in Windows to resolve '\' as python escape character
