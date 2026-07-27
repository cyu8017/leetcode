# LeetCode 1696 - Jump Game VI
# https://leetcode.com/problems/jump-game-vi/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_result(nums, k)
  q = [[0, nums[0]]]
  (1...nums.length).each do |i|
    q.shift while q[0][0] < i - k
    score = nums[i] + q[0][1]
    q.pop while !q.empty? && q[-1][1] <= score
    q << [i, score]
  end
  q[-1][1]
end
