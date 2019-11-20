import subprocess

subprocess.run(['java', '-jar', '[path to saxon - use \\ in filepath]', '-s:[path to source .xml file - use \\ in filepath]', '-xsl:[path to .xslt file - use \\ in filepath]', '-o:[path to output metadata files - use \\ in filepath]'], shell=True)
# temp use of \\ in Windows to resolve '\' as python escape character
