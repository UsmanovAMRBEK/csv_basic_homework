def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   
   return data.split('\n')[0].split(',')

# Read the csv file
f=open('data.csv','r')
data=f.read()
print(get_first_row(data))
f.close()