import sys ,unittest

# class A(unittest.TestCase):
#     result = {'test_001':False}
#     @classmethod
#     def setUpClass(cls):
#         super(A, cls).setUpClass()
#
#     def test_001(self):
#         self.result['test_001'] = False
#
#         print ('fffff',(self.result['test_001'] == True))
#
#     @unittest.skipIf(result['test_001'] == False, '跳过')
#     def test_002(self):
#         if self.result['test_001'] == True:
#             return
#         print ('test_002')
#
# if __name__ == '__main__':
#     unittest.main()

result = {'status':False}
print(result['status'] == 4)
