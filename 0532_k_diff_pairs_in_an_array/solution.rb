# LeetCode 0532 - K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution
  def find_pairs(nums, k)
    return 0 if k.negative?

    freq = Hash.new(0)
    nums.each { |num| freq[num] += 1 }

    pairs = 0
    freq.each_key do |num|
      if k.zero?
        pairs += 1 if freq[num] > 1
      elsif freq.key?(num + k)
        pairs += 1
      end
    end
    pairs
  end

  alias_method :findPairs, :find_pairs
end
