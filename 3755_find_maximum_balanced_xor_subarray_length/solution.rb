# LeetCode 3755 - Find Maximum Balanced XOR Subarray Length
# https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

# @param {Integer[]} nums
# @return {Integer}
def max_balanced_subarray(nums)
  d = {}
  a = 0
  b = nums.length
  ans = 0
  d[b] = -1
  nums.each_with_index do |x, i|
    a ^= x
    b += x.even? ? 1 : -1
    key = (a << 32) | (b & 0xFFFFFFFF)
    if d.key?(key)
      ans = [ans, i - d[key]].max
    else
      d[key] = i
    end
  end
  ans
end
