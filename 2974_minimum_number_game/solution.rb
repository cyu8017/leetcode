# LeetCode 2974 - Minimum Number Game
# https://leetcode.com/problems/minimum-number-game/

# @param {Integer[]} nums
# @return {Integer[]}
def number_game(nums)
  nums.sort!
  i = 0
  while i + 1 < nums.length
    nums[i], nums[i + 1] = nums[i + 1], nums[i]
    i += 2
  end
  nums
end
