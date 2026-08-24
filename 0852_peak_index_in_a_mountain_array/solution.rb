# LeetCode 0852 - Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# @param {Integer[]} arr
# @return {Integer}
def peak_index_in_mountain_array(arr)
  lo = 0
  hi = arr.length - 1
  while lo < hi
    mid = (lo + hi) / 2
    if arr[mid] < arr[mid + 1]
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end
