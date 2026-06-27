class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        colos=len(mat[0])
        if rows*colos!=r*c:
            return mat

        result=[]
        for k in mat:
            for h in k:
                result.append(h)

        reshape=[] 
        f=0       
        for i in range(r):
            resul=[]
            for j in range(c):
                resul.append(result[f])
                f+=1
            reshape.append(resul)  
        return reshape
