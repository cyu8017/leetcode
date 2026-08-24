# LeetCode 2149 - Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

# @param {Integer[]} nums
# @return {Integer[]}
def rearrange_array(nums)
  ans = Array.new(nums.length)
  pos = 0
  neg = 1
  nums.each do |x|
    if x > 0
      ans[pos] = x
      pos += 2
    else
      ans[neg] = x
      neg += 2
    end
  end
  ans
end
