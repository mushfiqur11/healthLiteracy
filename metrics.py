from readability import Readability
import numpy as np

text_to_grade = {
    'college_graduate': 16,
    'college': 13
}

def combined_readability(text, verbose=False):
    rd = Readability(text)
    g_list = []
    
    try:
        g = rd.flesch_kincaid().grade_level
        if g in text_to_grade:
            g = text_to_grade[g]
        else:
            g = int(g)
        g_list.append(g)
    except Exception as e:
        if verbose:
            print(f'flesch_kincaid: {e}')
    
    try:
        g = rd.ari().grade_levels[0]
        if g in text_to_grade:
            g = text_to_grade[g]
        else:
            g = int(g)
        g_list.append(g)
    except Exception as e:
        if verbose:
            print(f'ari: {e}')
    

    try:
        g = rd.coleman_liau().grade_level
        if g in text_to_grade:
            g = text_to_grade[g]
        else:
            g = int(g)
        g_list.append(g)
    except Exception as e:
        if verbose:
            print(f'coleman_liau: {e}')
    
    try:
        g = rd.gunning_fog().grade_level
        if g in text_to_grade:
            g = text_to_grade[g]
        else:
            g = int(g)
        g_list.append(g)
    except Exception as e:
        if verbose:
            print(f'gunning_fog: {e}')

    try:
        g = rd.smog().grade_level
        if g in text_to_grade:
            g = text_to_grade[g]
        else:
            g = int(g)
        g_list.append(g)
    except Exception as e:
        if verbose:
            print(f'smog: {e}')
    
    if len(g_list) == 0:
        return None

    mean_grade = int(np.mean(np.array(g_list)))
    return mean_grade


