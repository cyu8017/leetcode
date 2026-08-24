# LeetCode 0673 - Number of Longest Increasing Subsequence
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

# @param {Integer[]} nums
# @return {Integer}
def find_number_of_lis(nums)
  n = nums.length
  lengths = Array.new(n, 1)
  counts = Array.new(n, 1)
  n.times do |i|
    i.times do |j|
      next if nums[j] >= nums[i]

      if lengths[j] + 1 > lengths[i]
        lengths[i] = lengths[j] + 1
        counts[i] = counts[j]
      elsif lengths[j] + 1 == lengths[i]
        counts[i] += counts[j]
      end
    end
  end
  longest = lengths.max
  lengths.zip(counts).sum { |length, c| length == longest ? c : 0 }
end
