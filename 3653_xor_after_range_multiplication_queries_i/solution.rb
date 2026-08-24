# LeetCode 3653 - XOR After Range Multiplication Queries I
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def xor_after_queries(nums, queries)
  mod = 1_000_000_007
  queries.each do |l, r, k, v|
    idx = l
    while idx <= r
      nums[idx] = nums[idx] * v % mod
      idx += k
    end
  end
  ans = 0
  nums.each { |x| ans ^= x }
  ans
end
