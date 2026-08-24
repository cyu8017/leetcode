# LeetCode 2161 - Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

# @param {Integer[]} nums
# @param {Integer} pivot
# @return {Integer[]}
def pivot_array(nums, pivot)
  ans = Array.new(nums.length)
  i = 0
  nums.each do |x|
    if x < pivot
      ans[i] = x
      i += 1
    end
  end
  nums.each do |x|
    if x == pivot
      ans[i] = x
      i += 1
    end
  end
  nums.each do |x|
    if x > pivot
      ans[i] = x
      i += 1
    end
  end
  ans
end
