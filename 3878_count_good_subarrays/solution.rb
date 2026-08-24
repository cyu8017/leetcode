# LeetCode 3878 - Count Good Subarrays
# https://leetcode.com/problems/count-good-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def count_good_subarrays(nums)
  n = nums.length
  l = Array.new(n, -1)
  stk = []
  n.times do |i|
    x = nums[i]
    stk.pop while !stk.empty? && nums[stk[-1]] < x && (nums[stk[-1]] | x) == x
    l[i] = stk[-1] unless stk.empty?
    stk << i
  end
  r = Array.new(n, n)
  stk = []
  (n - 1).downto(0) do |i|
    stk.pop while !stk.empty? && (nums[stk[-1]] | nums[i]) == nums[i]
    r[i] = stk[-1] unless stk.empty?
    stk << i
  end
  ans = 0
  n.times { |i| ans += (i - l[i]) * (r[i] - i) }
  ans
end
