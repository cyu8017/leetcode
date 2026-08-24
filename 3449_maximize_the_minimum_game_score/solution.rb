# LeetCode 3449 - Maximize the Minimum Game Score
# https://leetcode.com/problems/maximize-the-minimum-game-score/

# @param {Integer[]} points
# @param {Integer} m
# @return {Integer}
def max_score(points, m)
  ok = lambda do |mid|
    need = 0
    extra = 0
    points.each do |p|
      req = (mid + p - 1) / p
      if req > extra
        visits = req - extra
        need += 2 * visits - 1
        extra = visits - 1
      else
        need += 1
        extra = 0
      end
      return false if need > m
    end
    need <= m
  end
  lo = 0
  hi = 10**18
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
