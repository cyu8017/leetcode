# LeetCode 1753 - Maximum Score From Removing Stones
# https://leetcode.com/problems/maximum-score-from-removing-stones/

# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def maximum_score(a, b, c)
  stones = [a, b, c].sort.reverse
  score = 0
  while stones[0] > 0 && stones[1] > 0
    stones[0] -= 1
    stones[1] -= 1
    score += 1
    stones = stones.sort.reverse
  end
  score
end
