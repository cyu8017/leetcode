# LeetCode 2100 - Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

# @param {Integer[]} security
# @param {Integer} time
# @return {Integer[]}
def good_days_to_rob_bank(security, time)
  n = security.length
  return (0...n).to_a if time == 0

  left = Array.new(n, 0)
  right = Array.new(n, 0)
  (1...n).each { |i| left[i] = left[i - 1] + 1 if security[i] <= security[i - 1] }
  (n - 2).downto(0) { |i| right[i] = right[i + 1] + 1 if security[i] <= security[i + 1] }
  (time...n - time).select { |i| left[i] >= time && right[i] >= time }
end
