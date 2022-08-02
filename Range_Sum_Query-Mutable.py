class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.old_sum = sum(self.nums)
        

    def update(self, index: int, val: int) -> None:
        self.old_sum -= self.nums[index]
        self.old_sum += val
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return self.old_sum - sum(self.nums[:left]) - sum(self.nums[right+1:])