# LeetCode 1726 - Tuple with Same Product
# https://leetcode.com/problems/tuple-with-same-product/

# @param {Integer[]} nums
# @return {Integer}
def tuple_same_product(nums)
  counts = Hash.new(0)
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each do |j|
      counts[nums[i] * nums[j]] += 1
    end
  end
  counts.values.sum { |count| count * (count - 1) * 4 }
end
