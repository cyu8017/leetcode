# LeetCode 3648 - Minimum Sensors to Cover Grid
# https://leetcode.com/problems/minimum-sensors-to-cover-grid/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_sensors(n, m, k)
  cover = 2 * k + 1
  ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
end
