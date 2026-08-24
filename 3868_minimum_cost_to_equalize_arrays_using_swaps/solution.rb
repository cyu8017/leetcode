# LeetCode 3868 - Minimum Cost to Equalize Arrays Using Swaps
# https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_cost(nums1, nums2)
  cnt2 = Hash.new(0)
  nums2.each { |x| cnt2[x] += 1 }
  cnt1 = Hash.new(0)
  nums1.each do |x|
    c = cnt2[x]
    if c > 0
      cnt2[x] = c - 1
    else
      cnt1[x] += 1
    end
  end
  ans = 0
  cnt1.each_value do |v|
    return -1 if v.odd?
    ans += v / 2
  end
  cnt2.each_value { |v| return -1 if v.odd? }
  ans
end
