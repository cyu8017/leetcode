# LeetCode 1394 - Find Lucky Integer In An Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/

def find_lucky(arr)
  counts = Hash.new(0)
  arr.each { |x| counts[x] += 1 }
  lucky = counts.select { |x, c| x == c }.keys
  lucky.empty? ? -1 : lucky.max
end
