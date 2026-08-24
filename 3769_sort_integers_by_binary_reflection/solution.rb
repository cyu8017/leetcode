# LeetCode 3769 - Sort Integers by Binary Reflection
# https://leetcode.com/problems/sort-integers-by-binary-reflection/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_by_reflection(nums)
  f = lambda do |x|
    y = 0
    while x != 0
      y = (y << 1) | (x & 1)
      x >>= 1
    end
    y
  end
  arr = nums.dup
  arr.sort_by! { |a| [f.call(a), a] }
  (0...nums.length).each { |i| nums[i] = arr[i] }
  nums
end
