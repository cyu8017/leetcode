# LeetCode 3002 - Maximum Size of a Set After Removals
# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximum_set_size(nums1, nums2)
  s1 = {}
  s2 = {}
  nums1.each { |x| s1[x] = true }
  nums2.each { |x| s2[x] = true }
  a = 0
  b = 0
  c = 0
  s1.each_key { |x| a += 1 unless s2[x] }
  s2.each_key do |x|
    if s1[x]
      c += 1
    else
      b += 1
    end
  end
  n = nums1.length
  a = [a, n / 2].min
  b = [b, n / 2].min
  [a + b + c, n].min
end
