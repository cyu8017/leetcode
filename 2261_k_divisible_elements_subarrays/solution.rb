# LeetCode 2261 - K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} p
# @return {Integer}
def count_distinct(nums, k, p)
  n = nums.length
  seen = {}
  n.times do |i|
    div = 0
    key = ""
    (i...n).each do |j|
      div += 1 if nums[j] % p == 0
      break if div > k

      key += "#{nums[j] + 1},"
      seen[key] = true
    end
  end
  seen.length
end
