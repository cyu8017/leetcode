# LeetCode 2612 - Minimum Reverse Operations
# https://leetcode.com/problems/minimum-reverse-operations/

# @param {Integer} n
# @param {Integer} p
# @param {Integer[]} banned
# @param {Integer} k
# @return {Integer[]}
def min_reverse_operations(n, p, banned, k)
  ban = {}
  banned.each { |x| ban[x] = true }
  ans = Array.new(n, -1)
  ans[p] = 0
  q = [[p, 0]]
  until q.empty?
    i, d = q.shift
    lo = i - (k - 1)
    lo = 0 if lo < 0
    hi = i
    hi = n - k if hi > n - k
    (lo..hi).each do |l|
      r = l + k - 1
      ni = l + r - i
      next if ni < 0 || ni >= n || ban[ni] || ans[ni] != -1

      ans[ni] = d + 1
      q << [ni, d + 1]
    end
  end
  ans
end
