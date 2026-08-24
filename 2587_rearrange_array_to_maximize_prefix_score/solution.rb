# LeetCode 2587 - Rearrange Array to Maximize Prefix Score
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
  nums = nums.sort
  s = 0
  ans = 0
  (nums.length - 1).downto(0) do |i|
    s += nums[i]
    break unless s > 0

    ans += 1
  end
  ans
end
