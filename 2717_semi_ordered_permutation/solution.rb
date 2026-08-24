# LeetCode 2717 - Semi-Ordered Permutation
# https://leetcode.com/problems/semi-ordered-permutation/

# @param {Integer[]} nums
# @return {Integer}
def semi_ordered_permutation(nums)
  n = nums.length
  p1 = 0
  pn = 0
  nums.each_with_index do |x, i|
    p1 = i if x == 1
    pn = i if x == n
  end
  ans = p1 + (n - 1 - pn)
  ans -= 1 if p1 > pn
  ans
end
