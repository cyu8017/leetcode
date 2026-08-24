# LeetCode 3847 - Find the Score Difference in a Game
# https://leetcode.com/problems/find-the-score-difference-in-a-game/

# @param {Integer[]} nums
# @return {Integer}
def score_difference(nums)
  ans = 0
  k = 1
  nums.each_with_index do |x, i|
    k = -k if x.odd?
    k = -k if i % 6 == 5
    ans += k * x
  end
  ans
end
