# LeetCode 2515 - Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

# @param {String[]} words
# @param {String} target
# @param {Integer} start_index
# @return {Integer}
def closest_target(words, target, start_index)
  n = words.length
  best = -1
  words.each_with_index do |w, i|
    next unless w == target

    d = i - start_index
    d = -d if d < 0
    d = n - d if n - d < d
    best = d if best < 0 || d < best
  end
  best
end
