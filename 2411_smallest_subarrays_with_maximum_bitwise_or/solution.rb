# LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

# @param {Integer[]} nums
# @return {Integer[]}
def smallest_subarrays(nums)
  n = nums.length
  ans = Array.new(n, 0)
  last = Array.new(32, -1)
  (n - 1).downto(0) do |i|
    (0...32).each { |b| last[b] = i if ((nums[i] >> b) & 1) != 0 }
    far = i
    (0...32).each { |b| far = last[b] if last[b] > far }
    ans[i] = far - i + 1
  end
  ans
end
