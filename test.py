# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 22:40:25 2022

@author: Xun.Zheng
"""

import unittest
import parse_symbol as ps


class TestPraseSymbolMethods(unittest.TestCase):
    
    '''
        Vaild Test Case
    '''
    def test_handle_vaild_dash(self):
        input_string = "8-10"
        input_scope = [0,20]
        expected_valid_output = [8,9,10]
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_vaild_comma(self):
        input_string = "8,10,17"
        input_scope = [0,20]
        expected_valid_output = [8,10,17]
        res = ps.parse_comma(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_vaild_slash(self):
        input_string = "6/2"
        input_scope = [0,10]
        expected_valid_output = [6,8,10]
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_vaild_star(self):
        input_string = "*"
        input_scope = [1,3]
        expected_valid_output = [1,2,3]
        res = ps.parse_star(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
    def test_handle_vaild_num(self):
        input_string = "32"
        input_scope = [1,59]
        expected_valid_output = [32]
        res = ps.parse_num(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
        
        '''
            InVaild Test Case
        '''       
    def test_handle_invaild_dash0(self):
        input_string = "8--10"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_invaild_dash1(self):
        input_string = "8-10,11"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_invaild_dash3(self):
        input_string = "*-10"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_invaild_dash4(self):
        input_string = "/8-10"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_outOfRange_dash(self):
        input_string = "8-10"
        input_scope = [9,10]
        expected_valid_output = "Out_Of_Range"
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_startGreaterEnd_dash(self):
        input_string = "10-8"
        input_scope = [1,20]
        expected_valid_output = "Start_Greater_End" 
        res = ps.parse_dash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
        
        
        
        
        
        
    def test_handle_invaild_comma0(self):
        input_string = "8,10,17,"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_comma(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)       
    
    def test_handle_invaild_comma1(self):
        input_string = "8,10,,17,"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_comma(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)  
    
    def test_handle_invaild_comma2(self):
        input_string = "*8,10,17,"
        input_scope = [0,20]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_comma(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)  
    
    def test_handle_outOfRange_comma(self):
        input_string = "8,10,12"
        input_scope = [1,10]
        expected_valid_output = "Out_Of_Range"
        res = ps.parse_comma(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
        
        
        
        
        
           
        
        
    def test_handle_invaild_slash0(self):
        input_string = "6//2"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
    def test_handle_invaild_slash1(self):
        input_string = "6/*"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
    def test_handle_invaild_slash2(self):
        input_string = "*6/10"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)  
        
    def test_handle_invaild_slash3(self):
        input_string = "6/-2"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)     
        
    def test_handle_outOfRange_slash(self):
        input_string = "6/10"
        input_scope = [7,10]
        expected_valid_output = "Out_Of_Range"
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)  

    def test_handle_outOfRange_slash1(self):
        input_string = "6/10"
        input_scope = [2,8]
        expected_valid_output = "Out_Of_Range"
        res = ps.parse_slash(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)  








    def test_handle_invaild_star0(self):
        input_string = "**"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_star(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)

    def test_handle_invaild_star1(self):
        input_string = "*/"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_star(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
    def test_handle_invaild_star2(self):
        input_string = "*10"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_star(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
        
        
    def test_handle_invaild_num0(self):
        input_string = "-1"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_num(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)

    def test_handle_invaild_num1(self):
        input_string = "9,"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_num(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
    
    def test_handle_invaild_num2(self):
        input_string = "#9,"
        input_scope = [1,10]
        expected_valid_output = "InVaild_Format"
        res = ps.parse_num(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
    def test_handle_outOfRange_num(self):
        input_string = "11"
        input_scope = [1,10]
        expected_valid_output = "Out_Of_Range"
        res = ps.parse_num(input_string, input_scope)
        self.assertEqual(res, expected_valid_output)
        
        
        
        
if __name__ == '__main__':
    unittest.main()
