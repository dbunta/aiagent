
import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

class TestGetFilesInfo(unittest.TestCase):
    # def setUp(self):
    #     pass
    #     #self.calculator = Calculator()

    # def test_get_files_info(self):
    #     result = get_files_info("calculator", "/bin")
    #     self.assertIn("Error", result)
    #     # print(result)
    #     result = get_files_info("calculator", "../")
    #     self.assertIn("Error", result)
    #     # print(result)
    #     result = get_files_info("calculator", ".")
    #     self.assertNotIn("Error", result)
    #     # print(result)
    #     result = get_files_info("calculator", "pkg")
    #     # print(result)
    #     self.assertNotIn("Error", result)
    
    # def test_get_file_content(self):
    #     result = get_file_content("calculator", "main.py")
    #     print(result)
    #     result = get_file_content("calculator", "pkg/calculator.py")
    #     print(result)
    #     result = get_file_content("calculator", "/bin/cat")
    #     print(result)

    def test_write_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)


if __name__ == "__main__":
    unittest.main()