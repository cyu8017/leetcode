# LeetCode 1471 - The K Strongest Values In An Array
# https://leetcode.com/problems/the-k-strongest-values-in-an-array/

def get_strongest(arr, k)
  arr.sort!
  median = arr[(arr.length - 1) / 2]
  arr.sort_by { |x| [-(x - median).abs, -x] }.first(k)
end
