# LeetCode 2176 - Count Equal and Divisible Pairs in an Array
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_pairs(nums, k)
  ans = 0
  nums.each_index do |i|
    ((i + 1)...nums.length).each do |j|
      ans += 1 if nums[i] == nums[j] && (i * j) % k == 0
    end
  end
  ans
end
