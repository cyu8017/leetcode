# LeetCode 3917 - Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/

# @param {Integer[]} nums
# @return {Integer[]}
def count_opposite_parity(nums)
  cnt = [0, 0]
  nums.each { |x| cnt[x & 1] += 1 }
  n = nums.length
  ans = Array.new(n, 0)
  n.times do |i|
    x = nums[i]
    cnt[x & 1] -= 1
    ans[i] = cnt[(x & 1) ^ 1]
  end
  ans
end
