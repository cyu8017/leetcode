# LeetCode 0927 - Three Equal Parts
# https://leetcode.com/problems/three-equal-parts/

# @param {Integer[]} arr
# @return {Integer[]}
def three_equal_parts(arr)
  ones = []
  arr.each_with_index { |bit, i| ones << i if bit != 0 }
  n = ones.length
  return [-1, -1] if n % 3 != 0
  return [0, arr.length - 1] if n == 0

  third = n / 3
  length = ones[-1] - ones[2 * third] + 1
  if arr[ones[0], length] == arr[ones[third], length] &&
     arr[ones[third], length] == arr[ones[2 * third]..]
    return [ones[0] + length - 1, ones[third] + length]
  end

  [-1, -1]
end
