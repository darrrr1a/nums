def find_missing_nums(nums):
    missing_nums = []

    for i in range(1, len(nums)):
        if i not in nums:
            missing_nums.append(i)

    return missing_nums