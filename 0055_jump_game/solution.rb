# LeetCode 0055 - Jump Game
# https://leetcode.com/problems/jump-game/

# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
  farthest = 0

  nums.each_with_index do |jump, i|
    return false if i > farthest

    farthest = [farthest, i + jump].max
  end

  true
end
