from string import Template

sample_str = "This is $going $great year"
the_template = Template(sample_str)
output_str = the_template.substitute(going='fox', great='jumped')
print(output_str)