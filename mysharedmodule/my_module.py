# Container3
# The shared Python Module
# 

'''
This code defines a simple function that takes in some data and performs some processing on it. 
This function could be used by both the Flask and Python libraries containers to perform the same processing on shared data.
'''

def my_shared_function(data):
# Do some processing on the data
  message = "processed the data[" + data + "]"
  print(f'data={message}')
  html=data.to_html()
  return html
