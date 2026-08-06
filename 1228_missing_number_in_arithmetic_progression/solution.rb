# LeetCode 1228 - Missing Number In Arithmetic Progression
# https://leetcode.com/problems/missing-number-in-arithmetic-progression/

# @param {Integer[]} arr
# @return {Integer}
def missing_number(arr)
  difference = (arr[-1] - arr[0]) / arr.length
  (1...arr.length).each do |i|
    expected = arr[0] + i * difference
    return expected if arr[i] != expected
  end
  arr[0]
end
