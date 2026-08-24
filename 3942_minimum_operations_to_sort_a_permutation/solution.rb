# LeetCode 3942 - Minimum Operations To Sort A Permutation
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  check = lambda do |zero, step|
    n = nums.length
    (1...n).each do |i|
      prev = ((zero + (i - 1) * step) % n + n) % n
      curr = ((zero + i * step) % n + n) % n
      return false if nums[prev] > nums[curr]
    end
    true
  end
  n = nums.length
  zero = nums.index(0)
  ans = 2_147_483_647
  if check.call(zero, 1)
    ans = [ans, zero].min
    ans = [ans, n - zero + 2].min
  end
  if check.call(zero, -1)
    ans = [ans, zero + 2].min
    ans = [ans, n - zero].min
  end
  ans == 2_147_483_647 ? -1 : ans
end
