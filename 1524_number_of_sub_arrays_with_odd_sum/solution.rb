# LeetCode 1524 - Number of Sub-arrays With Odd Sum
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

# @param {Integer[]} arr
# @return {Integer}
def num_of_subarrays(arr)
  counts = [1, 0]
  parity = answer = 0
  arr.each do |value|
    parity ^= value & 1
    answer += counts[parity ^ 1]
    counts[parity] += 1
  end
  answer % 1_000_000_007
end
