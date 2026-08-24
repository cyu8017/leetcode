# LeetCode 2143 - Choose Numbers From Two Arrays in Range
# https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def count_subranges(nums1, nums2)
  mod = 1_000_000_007
  n = nums1.length
  ans = 0
  dp = {}
  n.times do |i|
    ndp = Hash.new(0)
    ndp[nums1[i]] = (ndp[nums1[i]] + 1) % mod
    ndp[-nums2[i]] = (ndp[-nums2[i]] + 1) % mod
    dp.each do |diff, cnt|
      ndp[diff + nums1[i]] = (ndp[diff + nums1[i]] + cnt) % mod
      ndp[diff - nums2[i]] = (ndp[diff - nums2[i]] + cnt) % mod
    end
    dp = ndp
    ans = (ans + (dp[0] || 0)) % mod
  end
  ans
end
