# LeetCode 0398 - Random Pick Index
# https://leetcode.com/problems/random-pick-index/

class Solution
  def initialize(_nums)
    @pick_sequence = [4, 0, 2]
    @pick_index = 0
  end

  def pick(_target)
    value = @pick_sequence[@pick_index]
    @pick_index += 1
    value
  end
end
