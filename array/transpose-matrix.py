class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans=[]
        for i in range(len(matrix[0])):
            result=[]
            for j in range(len(matrix)):
                result.append(matrix[j][i])
            trans.append(result)
        return trans
