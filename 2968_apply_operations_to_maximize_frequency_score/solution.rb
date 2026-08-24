# LeetCode 2968 - Apply Operations to Maximize Frequency Score
# https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency_score(nums, k)
  nums.sort!
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 1
  left = 0
  n.times do |right|
    left += 1 while cost_range(nums, pref, left, right) > k
    ans = right - left + 1 if right - left + 1 > ans
  end
  ans
end

def cost_range(nums, pref, l, r)
  mid = (l + r) >> 1
  left = nums[mid] * (mid - l) - (pref[mid] - pref[l])
  right = (pref[r + 1] - pref[mid + 1]) - nums[mid] * (r - mid)
  left + right
end
