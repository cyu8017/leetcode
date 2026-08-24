# LeetCode 2293 - Min Max Game
# https://leetcode.com/problems/min-max-game/

# @param {Integer[]} nums
# @return {Integer}
def min_max_game(nums)
  while nums.length > 1
    nxt = Array.new(nums.length >> 1)
    nxt.length.times do |i|
      nxt[i] = if i.even?
                 [nums[2 * i], nums[2 * i + 1]].min
               else
                 [nums[2 * i], nums[2 * i + 1]].max
               end
    end
    nums = nxt
  end
  nums[0]
end
