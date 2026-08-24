# LeetCode 0922 - Sort Array By Parity II
# https://leetcode.com/problems/sort-array-by-parity-ii/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_array_by_parity_ii(nums)
  n = nums.length
  ans = Array.new(n, 0)
  even = 0
  odd = 0
  nums.each do |x|
    if x.even?
      ans[even] = x
      even += 2
    else
      ans[odd + 1] = x
      odd += 2
    end
  end
  ans
end
