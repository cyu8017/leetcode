# LeetCode 1207 - Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

# @param {Integer[]} arr
# @return {Boolean}
def unique_occurrences(arr)
  count = Hash.new(0)
  arr.each { |x| count[x] += 1 }
  vals = count.values
  vals.length == vals.uniq.length
end
