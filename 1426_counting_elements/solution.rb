# LeetCode 1426 - Counting Elements
# https://leetcode.com/problems/counting-elements/

def count_elements(arr)
  values = {}
  arr.each { |v| values[v] = true }
  arr.count { |value| values[value + 1] }
end
