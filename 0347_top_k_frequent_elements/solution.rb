# LeetCode 0347 - Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution
  def top_k_frequent(nums, k)
    counts = Hash.new(0)
    nums.each { |num| counts[num] += 1 }

    buckets = Array.new(nums.length + 1) { [] }
    counts.each do |value, count|
      buckets[count] << value
    end

    result = []
    (buckets.length - 1).downto(0) do |index|
      buckets[index].each do |value|
        result << value
        return result if result.length == k
      end
    end

    result
  end

  alias_method :topKFrequent, :top_k_frequent
end
