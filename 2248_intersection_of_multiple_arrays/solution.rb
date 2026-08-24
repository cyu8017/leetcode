# LeetCode 2248 - Intersection of Multiple Arrays
# https://leetcode.com/problems/intersection-of-multiple-arrays/

# @param {Integer[][]} nums
# @return {Integer[]}
def intersection(nums)
  freq = Hash.new(0)
  nums.each do |arr|
    seen = {}
    arr.each do |x|
      next if seen.key?(x)

      seen[x] = true
      freq[x] += 1
    end
  end
  freq.select { |_k, v| v == nums.length }.keys.sort
end
