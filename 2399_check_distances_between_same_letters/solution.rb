# LeetCode 2399 - Check Distances Between Same Letters
# https://leetcode.com/problems/check-distances-between-same-letters/

# @param {String} s
# @param {Integer[]} distance
# @return {Boolean}
def check_distances(s, distance)
  first = Array.new(26, -1)
  s.each_char.with_index do |ch, i|
    c = ch.ord - 97
    if first[c] == -1
      first[c] = i
    elsif i - first[c] - 1 != distance[c]
      return false
    end
  end
  true
end
