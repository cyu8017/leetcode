# LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
# https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_even_sum(nums, k)
  arr = nums.sort.reverse
  s = arr[0...k].sum
  return s if s.even?

  ans = -1
  odd_in = even_in = odd_out = even_out = -1
  (k - 1).downto(0) do |i|
    odd_in = i if arr[i].odd? && odd_in == -1
    even_in = i if arr[i].even? && even_in == -1
  end
  (k...arr.length).each do |i|
    odd_out = i if arr[i].odd? && odd_out == -1
    even_out = i if arr[i].even? && even_out == -1
  end
  ans = [ans, s - arr[odd_in] + arr[even_out]].max if odd_in != -1 && even_out != -1
  ans = [ans, s - arr[even_in] + arr[odd_out]].max if even_in != -1 && odd_out != -1
  ans
end
