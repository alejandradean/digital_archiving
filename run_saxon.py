import subprocess

subprocess.call(['java', '-jar', 'C:\\Program Files\\saxon9he.jar', '-s:C:\\Users\\Marcela Davison\\Desktop\\converted.xml', '-xsl:C:\\Users\\Marcela Davison\\Desktop\\hs6_07_1411.xsl', '-o:C:\\Users\\Marcela Davison\\Desktop\\metadata\\output.xml'], shell=True)
