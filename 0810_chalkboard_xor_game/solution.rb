# LeetCode 0810 - Chalkboard XOR Game
# https://leetcode.com/problems/chalkboard-xor-game/

# @param {Integer[]} nums
# @return {Boolean}
def xor_game(nums)
  nums.reduce(0, :^).zero? || nums.length.even?
end
