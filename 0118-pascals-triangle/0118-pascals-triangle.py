class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
     
        triangle = [[1]]
        
        for i in range(1, numRows):
            row = [1]
            prev_row = triangle[-1]
            
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            
            row.append(1)
            triangle.append(row)
        
        return triangle