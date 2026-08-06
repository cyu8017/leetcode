# LeetCode 1562 - Find Latest Group of Size M
# https://leetcode.com/problems/find-latest-group-of-size-m/

# @param {Integer[]} arr
# @param {Integer} m
# @return {Integer}
def find_latest_step(arr, m)
  return m if m == arr.length
  lengths = {}
  answer = -1
  arr.each_with_index do |x, idx|
    step = idx + 1
    left = lengths[x - 1] || 0
    right = lengths[x + 1] || 0
    size = left + 1 + right
    lengths[x - left] = lengths[x + right] = size
    answer = step - 1 if left == m || right == m
  end
  answer
end
