# LeetCode 3471 - Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_integer(nums, k)
  n = nums.length
  cnt = Hash.new(0)
  (0..(n - k)).each do |i|
    seen = {}
    (i...(i + k)).each { |j| seen[nums[j]] = true }
    seen.each_key { |x| cnt[x] += 1 }
  end
  ans = -1
  cnt.each do |key, value|
    ans = key if value == 1 && key > ans
  end
  ans
end
