# LeetCode 2053 - Kth Distinct String in an Array
# https://leetcode.com/problems/kth-distinct-string-in-an-array/

# @param {String[]} arr
# @param {Integer} k
# @return {String}
def kth_distinct(arr, k)
  freq = Hash.new(0)
  arr.each { |s| freq[s] += 1 }
  arr.each do |s|
    next unless freq[s] == 1

    k -= 1
    return s if k.zero?
  end
  ""
end
