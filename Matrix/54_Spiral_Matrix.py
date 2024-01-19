class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        rows = len(matrix)
        columns = len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, columns - 1
        d = 0

        while left <= right and top <= bottom:
            if d == 0:
                for i in range(left, right + 1):  # Include right in the range
                    result.append(matrix[top][i])
                top += 1
                d = 1
            elif d == 1:
                for i in range(top, bottom + 1):  # Include bottom in the range
                    result.append(matrix[i][right])
                right -= 1
                d = 2
            elif d == 2:
                for i in range(right, left - 1, -1):  # Include left in the range, decrement i
                    result.append(matrix[bottom][i])
                bottom -= 1
                d = 3
            elif d == 3:
                for i in range(bottom, top - 1, -1):  # Include top in the range, decrement i
                    result.append(matrix[i][left])
                left += 1
                d = 0
        return result
