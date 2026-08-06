# LeetCode 1191 - K-Concatenation Maximum Sum
# https://leetcode.com/problems/k-concatenation-maximum-sum/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def k_concatenation_max_sum(arr, k)
  mod = 10**9 + 7
  kadane = lambda do |nums|
    best = cur = 0
    nums.each do |x|
      cur = [0, cur + x].max
      best = [best, cur].max
    end
    best
  end
  one = kadane.call(arr)
  return one % mod if k == 1
  two = kadane.call(arr + arr)
  total = arr.sum
  if total > 0
    [one, two + total * (k - 2)].max % mod
  else
    [one, two].max % mod
  end
end
