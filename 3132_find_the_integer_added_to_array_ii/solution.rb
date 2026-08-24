# LeetCode 3132 - Find the Integer Added to Array II
# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_added_integer(nums1, nums2)
  nums1 = nums1.sort
  nums2 = nums2.sort

  ok = lambda do |x|
    i = 0
    j = 0
    cnt = 0
    while i < nums1.length && j < nums2.length
      if nums2[j] - nums1[i] != x
        cnt += 1
      else
        j += 1
      end
      i += 1
    end
    cnt <= 2
  end

  ans = 1 << 30
  3.times do |t|
    x = nums2[0] - nums1[t]
    ans = [ans, x].min if ok.call(x)
  end
  ans
end
