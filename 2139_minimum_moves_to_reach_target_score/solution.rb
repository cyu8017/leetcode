# LeetCode 2139 - Minimum Moves to Reach Target Score
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

# @param {Integer} target
# @param {Integer} max_doubles
# @return {Integer}
def min_moves(target, max_doubles)
  ans = 0
  while target > 1 && max_doubles > 0
    if target.odd?
      target -= 1
      ans += 1
    else
      target /= 2
      max_doubles -= 1
      ans += 1
    end
  end
  ans + target - 1
end
