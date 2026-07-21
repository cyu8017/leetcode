# LeetCode 1885 - Count Pairs in Two Arrays
# https://leetcode.com/problems/count-pairs-in-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def count_pairs(nums1, nums2)
  diff = nums1.zip(nums2).map { |a, b| a - b }.sort
  answer = 0
  n = diff.length

  (0...n).each do |i|
    target = -diff[i]
    # count of values > target in diff[i+1..]
    lo = i + 1
    hi = n
    while lo < hi
      mid = (lo + hi) / 2
      if diff[mid] > target
        hi = mid
      else
        lo = mid + 1
      end
    end
    answer += n - lo
  end

  answer
end
