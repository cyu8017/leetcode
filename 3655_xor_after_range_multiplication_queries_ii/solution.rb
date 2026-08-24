# LeetCode 3655 - XOR After Range Multiplication Queries II
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def xor_after_queries(nums, queries)
  mod = 1_000_000_007
  n = nums.length
  by_k = {}
  queries.each { |q| (by_k[q[2]] ||= []) << q }
  res = nums.dup
  by_k.each_value do |lst|
    fac = Array.new(n, 1)
    lst.each do |u|
      i = u[0]
      while i <= u[1]
        fac[i] = fac[i] * u[3] % mod
        i += u[2]
      end
    end
    (0...n).each { |i| res[i] = res[i] * fac[i] % mod }
  end
  ans = 0
  res.each { |v| ans ^= v }
  ans
end
