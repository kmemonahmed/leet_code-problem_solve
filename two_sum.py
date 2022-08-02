class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        to_return = []
        output = []
        for i in nums:
            new_arr = nums.copy()
            new_arr.remove(i)
            
            for j in new_arr:
                new_number = 0
                new_number = i +j
                if new_number == target:
                    to_return.append(i)
                    to_return.append(j)
                    break
                else:
                    continue
            if len(to_return) > 0:
                break
        
        if to_return[0] == to_return[1]:
            for i in to_return:
                output.append(nums.index(i))
                if len(output) > 0:
                    return [nums.index(to_return[0]), nums.index(to_return[1], output[0] + 1)]
                else:
                    pass
        else:
            return [nums.index(to_return[0]), nums.index(to_return[1])]
