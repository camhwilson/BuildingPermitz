import Levenshtein

from datetime import datetime, timedelta


def match_pct(str1, str2):
    str1 = str(str1).lower()
    str2 = str(str2).lower()
    normalized_factor = Levenshtein.distance(str1, str2)
    li_len = [len(i) for i in [str1, str2]]
    max_int = max(li_len)
    return (1-normalized_factor/max_int)*100



def date_valid(gc_date, date_in_question, timespan):
    #timespan is in years, function searches to see if date in question is in range specified
    timespan_days_half = timespan/2

    datetime_gc_date = datetime.strptime(gc_date,'%m/%d/%Y')
    
    datetime_date_in_question = datetime.strptime(date_in_question,'%m/%d/%Y')

    lower_bound = datetime_gc_date- timedelta(days=timespan_days_half)
    upper_bound = datetime_gc_date+ timedelta(days=timespan_days_half)

    if lower_bound < datetime_date_in_question < upper_bound:
        return True
    else:
        return False



