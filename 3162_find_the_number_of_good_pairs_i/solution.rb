# LeetCode 3162 - Find the Number of Good Pairs I
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def number_of_pairs(nums1, nums2, k)
  ans = 0
  nums1.each do |x|
    nums2.each { |y| ans += 1 if x % (y * k) == 0 }
  end
  ans
end
