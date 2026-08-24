# LeetCode 2475 - Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

# @param {Integer[]} nums
# @return {Integer}
def unequal_triplets(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  ans = 0
  left = 0
  n = nums.length
  cnt.each_value do |c|
    right = n - left - c
    ans += left * c * right
    left += c
  end
  ans
end
