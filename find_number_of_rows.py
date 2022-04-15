def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    return len(data.split('\n'))-1

# Read the csv file
f=open('data.csv','r')
data=f.read()
print(find_number_of_rows(data))
f.close()
