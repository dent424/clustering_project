# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:55:37 2015

@author: Alexander
"""

def recode_dict():
    translate = {
    0 : {'2':2,'NaN':'NaN','What is best for the country':1,'3':3,'4':4,'Own narrow interests':5},
    1 : {'Too much':3,'NaN':'NaN','Too little':1,'About right':2},
    2 : {'Strongly favor':1,'NaN':'NaN','Favor':2,'Oppose':4,'Strongly oppose':5,'Neither favor nor oppose':3},
    3 : {'A great deal':3, 'Hardly any':1, 'NaN':'NaN', 'Only some':2},
    4 : {'2':2,'3':3,'4':4,'NaN':'NaN','Not at all':5,'Very well':1,},
    5 : {},
    6 : {'NaN':'NaN','No':0,'Yes':1},
    7 : {'Fairly willing':2,'NaN':'NaN','Neither willing nor unwill':3,'Not at all willing':5,'Not very willing':4,'Very willing':1},
    8 : {'2':2,'3':3,'4':4,'NaN':'NaN','Not at all concerned':1,'Very concerned':5},
    9 : {'Moderately interest':2,'NaN':'NaN','Not at all interested':1,'Very interested':3},
    10 : {'Extremely dangerous for the environment':1,'NaN':'NaN','Not dangerous at all for the environment?':5,'Not very dangerous, or':4,'Somewhat dangerous':3,'Very dangerous':2},
    11 : {'Always':4,'NaN':'NaN','Never':1,'Often':3,'Sometimes':2},
    12 : {'NaN':'NaN','No, i have not':0,'Yes, i have':1},
    13 : {'A fair amount':3,'A great deal of influence':4, 'A little influence':2,'NaN':'NaN', 'None at all':1},
    14 : {'A great deal':4,'A little':2,'NaN':'NaN','Not at all':1, 'Some':3},
    15 : {},
    16 : {'Agree':4,'Disagree':2,'NaN':'NaN','Neither agree nor disagree':3,'Strongly agree':5,'Strongly disagree':1},
    17 : {},
    18 : {},
    19 : {'Dont lean one way or the other on this issue':3,'NaN':'NaN','Somewhat support opening antarctica':2,'Somewhat support reserving antarctica':4,'Strongly support opening antarctica':1,'Strongly support reserving antarctica':5},
    20 : {},
    21 : {'Extremely dangerous':1,'NaN':'NaN','Not dangerous':5,'Not very dangerous':4,'Somewhat dangerous':3,'Very dangerous':2},
    22 : {},
    23 : {'2':2,'3':3,'4':4,'Know a great deal':5,'Know nothing at all':1, 'NaN':'NaN'},
    24 : {'Agree':3,'Disagree':2,'NaN':'NaN','Strongly agree':4,'Strongly disagree':1},
    25 : {},
    26 : {'Conservative':2,'Extremely liberal':7,'Extrmly conservative':1,'Liberal':6,'Moderate':4,'NaN':'NaN','Slghtly conservative':3,'Slightly liberal':5},
    27 : {'2':2,'3':3,'4':4,'NaN':'NaN','Near complete agreement':1, 'No agreement at all':5},
    28 : {'Favor':3,'NaN':'NaN','Oppose':2,'Strongly favor':4,'Strongly oppose':1},
    29 : {'Agree':4,'Disagree':2,'NaN':'NaN','Neither agree nor disagree':3,'Agree strongly':5,'Disagree strongly':1},
    30 : {'Extremely dangerous for the environment':1,'NaN':'NaN','Not dangerous at all for the environment':5,'Not very dangerous':4,'Somewhat dangerous':3,'Very dangerous':2},
    31 : {'About the right amount, or':2, 'More than enough':3,'NaN':'NaN','Too little?':1},
    32 : {},
    33 : {},
    34 : {'89 or older':89}
    }
    
    return translate