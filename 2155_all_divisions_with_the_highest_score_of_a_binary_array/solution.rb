# LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

# @param {Integer[]} nums
# @return {Integer[]}
def max_score_indices(nums)
  n = nums.length
  total1 = nums.sum
  best = total1
  left0 = 0
  right1 = total1
  ans = [0]
  n.times do |i|
    if nums[i] == 0
      left0 += 1
    else
      right1 -= 1
    end
    score = left0 + right1
    if score > best
      best = score
      ans = [i + 1]
    elsif score == best
      ans << i + 1
    end
  end
  ans
end
