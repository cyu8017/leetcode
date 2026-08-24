# LeetCode 2960 - Count Tested Devices After Test Operations
# https://leetcode.com/problems/count-tested-devices-after-test-operations/

# @param {Integer[]} battery_percentages
# @return {Integer}
def count_tested_devices(battery_percentages)
  ans = 0
  battery_percentages.each { |b| ans += 1 if b > ans }
  ans
end
