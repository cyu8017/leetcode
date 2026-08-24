# LeetCode 2640 - Find the Score of All Prefixes of an Array
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def find_prefix_score(nums)
  ans = Array.new(nums.length, 0)
  mx = 0
  s = 0
  nums.each_with_index do |x, i|
    mx = x if x > mx
    s += x + mx
    ans[i] = s
  end
  ans
end
