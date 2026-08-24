# LeetCode 2613 - Beautiful Pairs
# https://leetcode.com/problems/beautiful-pairs/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def beautiful_pair(nums1, nums2)
  n = nums1.length
  best = Float::INFINITY
  ans = [0, 1]
  n.times do |i|
    (i + 1...n).each do |j|
      d = (nums1[i] - nums1[j]).abs + (nums2[i] - nums2[j]).abs
      if d < best || (d == best && (i < ans[0] || (i == ans[0] && j < ans[1])))
        best = d
        ans = [i, j]
      end
    end
  end
  ans
end

alias solve beautiful_pair
