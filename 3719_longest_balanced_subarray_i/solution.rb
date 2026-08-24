# LeetCode 3719 - Longest Balanced Subarray I
# https://leetcode.com/problems/longest-balanced-subarray-i/

# @param {Integer[]} nums
# @return {Integer}
def longest_balanced(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    vis = {}
    cnt = [0, 0]
    (i...n).each do |j|
      unless vis[nums[j]]
        vis[nums[j]] = true
        cnt[nums[j] & 1] += 1
      end
      ans = [ans, j - i + 1].max if cnt[0] == cnt[1]
    end
  end
  ans
end
