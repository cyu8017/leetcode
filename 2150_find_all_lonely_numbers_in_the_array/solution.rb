# LeetCode 2150 - Find All Lonely Numbers in the Array
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

# @param {Integer[]} nums
# @return {Integer[]}
def find_lonely(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  freq.filter_map { |k, v| k if v == 1 && !freq.key?(k - 1) && !freq.key?(k + 1) }
end
