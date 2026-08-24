# LeetCode 2790 - Maximum Number of Groups With Increasing Length
# https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

# @param {Integer[]} usage_limits
# @return {Integer}
def max_increasing_groups(usage_limits)
  arr = usage_limits.sort
  ans = 0
  total = 0
  arr.each do |v|
    total += v
    need = (ans + 1) * (ans + 2) / 2.0
    ans += 1 if total >= need
  end
  ans
end
