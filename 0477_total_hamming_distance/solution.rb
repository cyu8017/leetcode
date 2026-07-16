# LeetCode 0477 - Total Hamming Distance
# https://leetcode.com/problems/total-hamming-distance/

class Solution
  def total_hamming_distance(nums)
    total = 0
    32.times do |bit|
      zeros = 0
      ones = 0
      nums.each do |value|
        if value & (1 << bit) != 0
          ones += 1
        else
          zeros += 1
        end
      end
      total += zeros * ones
    end
    total
  end

  alias_method :totalHammingDistance, :total_hamming_distance
end
