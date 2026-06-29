    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]
        for i in range(len(matrix)):
            result=[]
            for j in range(len(matrix[i])):
                if matrix[i][j]==-1:
                    k=0
                    mux=0
                    while k<len(matrix):
                        mux=max(mux,matrix[k][j])
                        k+=1
                    result.append(mux)
                else:
                    result.append(matrix[i][j])
            answer .append(result)
        return answer
