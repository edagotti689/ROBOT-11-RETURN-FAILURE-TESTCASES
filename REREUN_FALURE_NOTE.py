# How do you run failure test cases only ?
By using --rerunfailed option we can run failure test cases only.

## Below is the example to run failure test cases
robot --output firstrun.xml testsuite.robot 

# To run only failure test cases based on first execution of output.xml
robot --rerunfailed firstrun.xml --output secondrun.xml testsuite.robot

# To merge first execution .xml file with second execution .xml file
rebot --merge firstrun.xml secondrun.xml

