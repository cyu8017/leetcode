# LeetCode 1477 - Find Two Non Overlapping Sub Arrays Each With Target Sum
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

def min_sum_of_lengths(arr, target)
  inf = 10**9
  left = total = 0
  best = ans = inf
  shortest = Array.new(arr.length, inf)
  arr.each_with_index do |x, right|
    total += x
    while total > target
      total -= arr[left]
      left += 1
    end
    if total == target
      length = right - left + 1
      ans = [ans, length + shortest[left - 1]].min if left > 0
      best = [best, length].min
    end
    shortest[right] = best
  end
  ans == inf ? -1 : ans
end
