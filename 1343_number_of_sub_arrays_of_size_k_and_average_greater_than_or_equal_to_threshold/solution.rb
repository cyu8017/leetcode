# LeetCode 1343 - Number Of Sub Arrays Of Size K And Average Greater Than Or Equal To Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

def num_of_subarrays(arr, k, threshold)
  window = arr.first(k).sum
  answer = window >= k * threshold ? 1 : 0
  (k...arr.length).each do |i|
    window += arr[i] - arr[i - k]
    answer += 1 if window >= k * threshold
  end
  answer
end
