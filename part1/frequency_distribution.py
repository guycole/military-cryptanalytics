#
#
#
from typing import List

class Solution:
    
    def reader(self, file_name: str) -> List[str]:
        buffer = []

        try:
            with open(file_name) as fp:
                buffer = fp.readlines()
        except Exception as error:
            print(error)

        return buffer

    def execute(self, file_name):
        buffer = self.reader(file_name)
        print(buffer)

if __name__ == '__main__':
    solution = Solution()
    solution.execute('aiw_english.txt')  

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***