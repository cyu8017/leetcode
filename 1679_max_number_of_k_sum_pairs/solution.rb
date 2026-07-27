# LeetCode 1679 - Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_operations(nums, k)
  c = Hash.new(0)
  ans = 0
  nums.each do |x|
    if c[k - x].positive?
      c[k - x] -= 1
      ans += 1
    else
      c[x] += 1
    end
  end
  ans
end
