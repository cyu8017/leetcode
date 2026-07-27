# LeetCode 1640 - Check Array Formation Through Concatenation
# https://leetcode.com/problems/check-array-formation-through-concatenation/

# @param {Integer[]} arr
# @param {Integer[][]} pieces
# @return {Boolean}
def can_form_array(arr, pieces)
  by_first = {}
  pieces.each { |p| by_first[p[0]] = p }
  i = 0
  while i < arr.length
    return false unless by_first.key?(arr[i])

    p = by_first[arr[i]]
    return false if arr[i, p.length] != p

    i += p.length
  end
  true
end
