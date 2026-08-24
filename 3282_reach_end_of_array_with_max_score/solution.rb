# LeetCode 3282 - Reach End of Array With Max Score
# https://leetcode.com/problems/reach-end-of-array-with-max-score/

# @param {Integer[]} nums
# @return {Integer}
def find_maximum_score(nums)
  ans = 0
  max_v = 0
  (0...(nums.length - 1)).each do |i|
    max_v = nums[i] if nums[i] > max_v
    ans += max_v
  end
  ans
end
