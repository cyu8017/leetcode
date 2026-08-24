# LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
# https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

# @param {Integer[]} capacity
# @return {Integer}
def count_stable_subarrays(capacity)
  n = capacity.length
  s = Array.new(n + 1, 0)
  (1..n).each { |i| s[i] = s[i - 1] + capacity[i - 1] }
  cnt = Hash.new(0)
  ans = 0
  (2...n).each do |r|
    l = r - 2
    key_l = [capacity[l], capacity[l] + s[l + 1]]
    cnt[key_l] += 1
    key_r = [capacity[r], s[r]]
    ans += cnt[key_r]
  end
  ans
end
