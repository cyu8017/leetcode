# LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

# @param {Integer[]} arr
# @return {Integer}
def find_special_integer(arr)
  n = arr.length
  [arr[n / 4], arr[n / 2], arr[3 * n / 4]].each do |value|
    return value if arr.count(value) > n / 4
  end
  arr[0]
end
