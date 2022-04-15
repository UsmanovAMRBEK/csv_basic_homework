def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    l=[]
    for i in data.split('\n'):
        if i != '':
            l.append(i.split(',')[0])
    return l
    
# Read the csv file
f=open('data.csv','r')
data=f.read()
print(get_first_column(data))
f.close()