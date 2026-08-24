# LeetCode 3679 - Minimum Discards to Balance Inventory
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/

# @param {Integer[]} arrivals
# @param {Integer} w
# @param {Integer} m
# @return {Integer}
def min_arrivals_to_discard(arrivals, w, m)
  cnt = Hash.new(0)
  n = arrivals.length
  marked = Array.new(n, 0)
  ans = 0
  (0...n).each do |i|
    x = arrivals[i]
    cnt[arrivals[i - w]] -= marked[i - w] if i >= w
    if cnt[x] >= m
      ans += 1
    else
      marked[i] = 1
      cnt[x] += 1
    end
  end
  ans
end
