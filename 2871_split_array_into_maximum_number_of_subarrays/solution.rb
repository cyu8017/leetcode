# LeetCode 2871 - Split Array Into Maximum Number of Subarrays
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def max_subarrays(nums)
  ans = 0
  cur = -1
  nums.each do |v|
    if cur == -1
      cur = v
    else
      cur &= v
    end
    if cur == 0
      ans += 1
      cur = -1
    end
  end
  ans == 0 ? 1 : ans
end
