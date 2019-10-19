import pandas as pd
import numpy as np


def MissingpolicyKey(user_role, access_policies, user_entitlement):
    list = user_role.merge(access_policies, how='left', on='Role')
    list.drop(columns='Role', inplace=True)
    columnsTitles = ['User', 'Entitlement', 'Policy']
    list = list.reindex(columns=columnsTitles)
    list2 = user_entitlement[user_entitlement.isnull().any(axis=1)]
    list3 = list2.merge(list, how='inner', on=['User', 'Entitlement']).drop(columns='Policy_x')
    print(list3)
    return list3




def updatingValues1():

    data = input("DataFrame for user_role ")
    user_role = pd.DataFrame(eval(data))
    # print(user_role)
    data1 = input("DataFrame for access_policies ")
    access_policies = pd.DataFrame(eval(data1))
    # print(access_policies)
    data2 = input("DataFrame for user_entitlement ")
    user_entitlement = pd.DataFrame(eval(data2))
    # print(user_entitlement)
    return user_role, access_policies, user_entitlement


def main():

    df1, df2, df3 = updatingValues1()
    MissingpolicyKey(df1, df2, df3)


if __name__ == '__main__':
    main()



