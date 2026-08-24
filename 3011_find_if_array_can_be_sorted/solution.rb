# LeetCode 3011 - Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/

# @param {Integer[]} nums
# @return {Boolean}
def can_sort_array(nums)
  pre_mx = 0
  i = 0
  n = nums.length
  while i < n
    cnt = popcount(nums[i])
    j = i + 1
    mi = nums[i]
    mx = nums[i]
    while j < n && popcount(nums[j]) == cnt
      mi = nums[j] if nums[j] < mi
      mx = nums[j] if nums[j] > mx
      j += 1
    end
    return false if pre_mx > mi

    pre_mx = mx
    i = j
  end
  true
end

def popcount(x)
  c = 0
  while x != 0
    c += x & 1
    x >>= 1
  end
  c
end
