def sum_nums(x: int, y: int):
    return x + y

def multiple_nums(x: int, y: int):
    return x * y

def get_minimum(nums: list):
    if len(nums) == 0:
        raise RuntimeError("List must not be empty")
    return min(nums)
