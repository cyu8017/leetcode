# LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

# @param {Integer[]} nums
# @return {Integer[][]}
def find_matrix(nums)
  freq = Hash.new(0)
  ans = []
  nums.each do |x|
    f = freq[x]
    ans << [] if f == ans.length
    ans[f] << x
    freq[x] = f + 1
  end
  ans[0].reverse! if ans.length == 1
  ans
end
