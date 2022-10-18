class BinarySearch:
    def search(self, nums: list[int], target: int):
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2
            if nums[middle] < target:
                start = middle + 1


            elif nums[middle] > target:
                end = middle - 1


            elif nums[middle] == target:

                return middle
        return -1