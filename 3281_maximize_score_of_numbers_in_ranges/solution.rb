# LeetCode 3281 - Maximize Score of Numbers in Ranges
# https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

# @param {Integer[]} start
# @param {Integer} d
# @return {Integer}
def max_possible_score(start, d)
  start.sort!
  n = start.length
  ok = lambda do |mid|
    prev = start[0]
    (1...start.length).each do |i|
      need = prev + mid
      cur = start[i]
      return false if need > cur + d
      prev = need > cur ? need : cur
    end
    true
  end
  lo = 0
  hi = start[n - 1] + d - start[0] + 1
  while lo < hi
    mid = (lo + hi + 1) / 2
    if ok.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
