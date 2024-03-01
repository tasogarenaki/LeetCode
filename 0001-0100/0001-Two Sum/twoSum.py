def twoSum(nums, target):

    """
    # for test
    >>> nums = [5,4,6,6]
    >>> target = 12
    >>> twoSum(nums,target)
    [2, 3]
    >>> nums = [3,2,4]
    >>> target = 6
    >>> twoSum(nums,target)
    [1, 2]
    """
    
    # solution 1
    # normal way, slow, calculate every times 
    """
    length = len(nums)
    result = []
    for i in range(length-1):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result 
    """

    # solution 2
    # quick, reduce calculate times by using enumerate() 
    """
    length = len(nums)
    for i, num in enumerate(nums):
        targ_num = target - num
        for j in range(i+1, length):
            if nums[j] == targ_num:
                return [i,j]
    """
            
    # solution 3
    # best solution by using HashTable
    dic = {}                                    # initial a dic
    for i, num in enumerate(nums):              
        targ_num = target - num                 # calc difference between targ and current value
        if targ_num in dic:                     # if the difference already in dic
            return [dic[targ_num], i]           # direct return the index of both nums 
        dic[num] = i                            # otherwise save the num in dic for next search


    

