def power_set(nums):
    def sub_power_set(current, nums):
        if not nums:
            return [current]
        
        return sub_power_set(current, nums[1:]) + sub_power_set(current + [nums[0]], nums[1:])

    return sub_power_set([], sorted(nums))

if __name__ == '__main__':
    print(power_set([1, 2, 3]))