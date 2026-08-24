# LeetCode 0697 - Degree of an Array
# https://leetcode.com/problems/degree-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def find_shortest_sub_array(nums)
  first = {}
  last = {}
  count = Hash.new(0)
  nums.each_with_index do |num, i|
    first[num] = i unless first.key?(num)
    last[num] = i
    count[num] += 1
  end

  degree = count.values.max
  count.filter_map { |num, freq| last[num] - first[num] + 1 if freq == degree }.min
end
