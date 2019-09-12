import unittest

from pandas.util.testing import assert_frame_equal

from UseCase import try1
import pandas as pd
import numpy as np

class TestCalc(unittest.TestCase):

    def test_case1(self):
        user_role = pd.DataFrame(({'User': ['User1', 'User1'], 'Role': ['Role1', 'Role2']}))
        access_policies = pd.DataFrame(({'Policy': ['Policy1', 'Policy2'], 'Role': ['Role1', 'Role2'],'Entitlement': ['Entitlement2', 'Entitlement1']}))
        user_entitlement = pd.DataFrame(({'User': ['User1', 'User1', 'User1'], 'Entitlement': ['Entitlement1', 'Entitlement2', 'Entitlement3'], 'Policy': [np.nan, 'Policy1', np.nan]}))
        check1 = try1.MissingpolicyKey(user_role, access_policies, user_entitlement)
        check = pd.DataFrame({'User': ['User1'], 'Entitlement': ['Entitlement1'], 'Policy_y': ['Policy2']})
        assert_frame_equal(check1, check)

    def test_case2(self):
        user_role = pd.DataFrame(({'User': ['User1', 'User1'], 'Role': ['Role1', 'Role2']}))
        access_policies = pd.DataFrame(({'Policy': ['Policy1', 'Policy2'], 'Role': ['Role1', 'Role2'],
                                         'Entitlement': ['Entitlement2', 'Entitlement1']}))
        user_entitlement = pd.DataFrame(({'User': ['User1', 'User1', 'User1'],
                                          'Entitlement': ['Entitlement1', 'Entitlement2', 'Entitlement3'],
                                          'Policy': [np.nan,np.nan,np.nan]}))
        check1 = try1.MissingpolicyKey(user_role, access_policies, user_entitlement)
        check = pd.DataFrame({'User': ['User1','User1'], 'Entitlement': ['Entitlement1','Entitlement2'], 'Policy_y': ['Policy2','Policy1']})
        assert_frame_equal(check1, check)

    def test_case3(self):
        user_role = pd.DataFrame(({'User': ['User1','User1','User2','User2'], 'Role': ['Role1','Role2','Role1','Role3']}))
        access_policies = pd.DataFrame(({'Policy': ['Policy1','Policy2','Policy1','Policy1','Policy3','Policy3'], 'Role': ['Role1','Role2','Role1','Role1','Role3','Role3'], 'Entitlement': ['Entitlement2' , 'Entitlement1','Entitlement2','Entitlement3','Entitlement1','Entitlement2']}))
        user_entitlement = pd.DataFrame(({'User': ['User1','User1' , 'User2','User2'], 'Entitlement': ['Entitlement1' , 'Entitlement2' , 'Entitlement3','Entitlement1'], 'Policy': ['Policy2','Policy1' ,np.nan, np.nan]}))
        check1 = try1.MissingpolicyKey(user_role, access_policies, user_entitlement)
        check = pd.DataFrame({'User': ['User2', 'User2'], 'Entitlement': ['Entitlement3', 'Entitlement1'],
                                                  'Policy_y': ['Policy1', 'Policy3']})
        assert_frame_equal(check1, check)

    def test_case4(self):
        user_role = pd.DataFrame(({'User': ['User1', 'User1'], 'Role': ['Role1', 'Role2']}))
        access_policies = pd.DataFrame(({'Policy': ['Policy1', 'Policy2'], 'Role': ['Role1', 'Role2'],
                                         'Entitlement': ['Entitlement2', 'Entitlement1']}))
        user_entitlement = pd.DataFrame(({'User': ['User1', 'User1', 'User1'],
                                          'Entitlement': ['Entitlement1', 'Entitlement2', 'Entitlement3'],
                                          'Policy': ['Policy2', 'Policy1', np.nan]}))
        check1 = try1.MissingpolicyKey(user_role, access_policies, user_entitlement)
        column_names = ['User', 'Entitlement' , 'Policy_y']
        check = pd.DataFrame(columns=column_names)
        assert_frame_equal(check1, check)






if __name__ == '__main__':
    unittest.main()
