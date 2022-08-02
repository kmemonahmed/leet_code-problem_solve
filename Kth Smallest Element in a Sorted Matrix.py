class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new_arr = []
        for i in matrix:
            new_arr+=i
        new_arr.sort()
        return new_arr[k-1]