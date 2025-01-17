def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    return len(data.split('\n')[0].split(','))

# Read the csv file
f=open('data.csv','r')
data=f.read()
print(find_number_of_columns(data))
f.close()
