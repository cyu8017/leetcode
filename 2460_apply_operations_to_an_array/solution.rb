# LeetCode 2460 - Apply Operations to an Array
# https://leetcode.com/problems/apply-operations-to-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def apply_operations(nums)
  n = nums.length
  a = nums.dup
  (0...(n - 1)).each do |i|
    if a[i] == a[i + 1]
      a[i] *= 2
      a[i + 1] = 0
    end
  end
  ans = Array.new(n, 0)
  j = 0
  a.each do |x|
    if x != 0
      ans[j] = x
      j += 1
    end
  end
  ans
end
