# LeetCode 1248 - Count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def number_of_subarrays(nums, k)
  frequency = Hash.new(0)
  frequency[0] = 1
  odd = answer = 0
  nums.each do |x|
    odd += x & 1
    answer += frequency[odd - k]
    frequency[odd] += 1
  end
  answer
end
