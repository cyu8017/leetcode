# LeetCode 2677 - Chunk Array
# https://leetcode.com/problems/chunk-array/

# @param {Object[]} arr
# @param {Integer} size
# @return {Object[][]}
def chunk(arr, size)
  ans = []
  i = 0
  while i < arr.length
    ans << arr[i, size]
    i += size
  end
  ans
end
