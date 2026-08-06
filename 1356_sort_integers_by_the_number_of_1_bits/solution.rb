# LeetCode 1356 - Sort Integers By The Number Of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

def sort_by_bits(arr)
  arr.sort_by { |x| [x.to_s(2).count('1'), x] }
end
