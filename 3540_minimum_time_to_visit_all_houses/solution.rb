# LeetCode 3540 - Minimum Time to Visit All Houses
# https://leetcode.com/problems/minimum-time-to-visit-all-houses/

# @param {Integer[]} forward
# @param {Integer[]} backward
# @param {Integer[]} queries
# @return {Integer}
def min_total_time(forward, backward, queries)
  n = forward.length
  sum_b = 0
  backward.each { |x| sum_b += x }
  pf = Array.new(n + 1, 0)
  pb = Array.new(n + 1, 0)
  (0...n).each do |i|
    pf[i + 1] = pf[i] + forward[i]
    pb[i + 1] = pb[i] + backward[i]
  end
  ans = 0
  pos = 0
  queries.each do |q|
    r = 0
    r = pf[n] if q < pos
    r += pf[q] - pf[pos]
    lft = 0
    lft = sum_b if q > pos
    lft += pb[pos] - pb[q]
    ans += [lft, r].min
    pos = q
  end
  ans
end
