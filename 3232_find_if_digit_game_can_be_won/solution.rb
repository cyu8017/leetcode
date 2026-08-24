# LeetCode 3232 - Find if Digit Game Can Be Won
# https://leetcode.com/problems/find-if-digit-game-can-be-won/

# @param {Integer[]} nums
# @return {Boolean}
def can_alice_win(nums)
  a = b = 0
  nums.each do |x|
    if x < 10
      a += x
    else
      b += x
    end
  end
  a != b
end
