# LeetCode 0624 - Maximum Distance in Arrays
# https://leetcode.com/problems/maximum-distance-in-arrays/

# @param {Integer[][]} arrays
# @return {Integer}
def max_distance(arrays)
  min_val = arrays[0][0]
  max_val = arrays[0][-1]
  best = 0
  arrays[1..].each do |arr|
    best = [best, (arr[-1] - min_val).abs, (max_val - arr[0]).abs].max
    min_val = [min_val, arr[0]].min
    max_val = [max_val, arr[-1]].max
  end
  best
end
