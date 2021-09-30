import Levenshtein

def match_pct(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    normalized_factor = Levenshtein.distance(str1, str2)
    li_len = [len(i) for i in [str1, str2]]
    max_int = max(li_len)
    return (1-normalized_factor/max_int)*100


def rename_cols(old_col_list, new_col_names):
    li = []
    for val1 in old_col_list:
        for val2 in new_col_names:
            percentage = match_pct(val1, val2)
            #May need to adjust match percentage
            if percentage > 40:
                li.append(val2)
                break
            if percentage < 40 and new_col_names[-1] == val2:
                li.append(str(val1) + ' (Extra Column)')
                break
    print(li)
    return li

def substring_in_list(string, list):
    condition = False
    for j in list:
        if string.lower() in str(j).lower():
            condition = True
    return condition

