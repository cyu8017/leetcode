# LeetCode 1144 - Decrease Elements To Make Array Zigzag
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

# @param {Integer[]} nums
# @return {Integer}
def moves_to_make_zigzag(nums)
  cost = lambda do |start|
    ans = 0
    start.step(nums.length - 1, 2) do |i|
      left = i > 0 ? nums[i - 1] : Float::INFINITY
      right = i + 1 < nums.length ? nums[i + 1] : Float::INFINITY
      ans += [0, nums[i] - [left, right].min + 1].max
    end
    ans
  end
  [cost.call(0), cost.call(1)].min
end
