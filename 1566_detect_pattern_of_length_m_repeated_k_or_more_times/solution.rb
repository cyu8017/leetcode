# LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

# @param {Integer[]} arr
# @param {Integer} m
# @param {Integer} k
# @return {Boolean}
def contains_pattern(arr, m, k)
  run = 0
  (m...arr.length).each do |i|
    run = arr[i] == arr[i - m] ? run + 1 : 0
    return true if run >= m * (k - 1)
  end
  false
end
