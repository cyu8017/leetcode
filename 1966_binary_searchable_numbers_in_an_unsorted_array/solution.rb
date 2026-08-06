# LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
# https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

# @param {Integer[]} nums
# @return {Integer}
def binary_searchable_numbers(nums)
  n = nums.length
  ok = Array.new(n, 1)
  mx = -Float::INFINITY
  mi = Float::INFINITY
  nums.each_with_index do |x, i|
    if x < mx
      ok[i] = 0
    else
      mx = x
    end
  end
  (n - 1).downto(0) do |i|
    if nums[i] > mi
      ok[i] = 0
    else
      mi = nums[i]
    end
  end
  ok.sum
end
