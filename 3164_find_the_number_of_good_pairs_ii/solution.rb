# LeetCode 3164 - Find the Number of Good Pairs II
# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def number_of_pairs(nums1, nums2, k)
  cnt1 = {}
  nums1.each do |x|
    if x % k == 0
      cnt1[x / k] = cnt1.fetch(x / k, 0) + 1
    end
  end
  return 0 if cnt1.empty?
  cnt2 = Hash.new(0)
  nums2.each { |x| cnt2[x] += 1 }
  mx = cnt1.keys.max
  ans = 0
  cnt2.each do |x, v|
    s = 0
    y = x
    while y <= mx
      c = cnt1[y]
      s += c unless c.nil?
      y += x
    end
    ans += s * v
  end
  ans
end
