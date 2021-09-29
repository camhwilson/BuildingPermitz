

#returns tuple containing coordinates of substring location within dataframe
def determine_shift(dataframe, string):
    condition = False
    rightshift = 0
    while condition == False:
        list1 = dataframe.iloc[:,rightshift].tolist()
        downshift = 0
        for j in list1:
            if string in str(j):
                condition = True
                return downshift, rightshift
            downshift+=1
        rightshift+=1


def determine_colshift(dataframe, string):
    condition = False
    rightshift = 0
    while condition == False:
        list1 = dataframe.iloc[:,rightshift].tolist()
        for j in list1:
            if string in str(j):
                condition = True
                return rightshift
        rightshift+=1

        
def determine_rowshift(dataframe, string):
    condition = False
    rightshift = 0
    while condition == False:
        list1 = dataframe.iloc[:,rightshift].tolist()
        downshift = 0
        for j in list1:
            if string in str(j):
                condition = True
                return downshift
            downshift+=1
        rightshift+=1


