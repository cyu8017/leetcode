# LeetCode 1619 - Mean of Array After Removing Some Elements
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

# @param {Integer[]} arr
# @return {Float}
def trim_mean(arr)
  arr = arr.sort
  k = arr.length / 20
  slice = arr[k...(arr.length - k)]
  slice.sum.to_f / slice.length
end
