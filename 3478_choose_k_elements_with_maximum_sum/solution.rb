# LeetCode 3478 - Choose K Elements With Maximum Sum
# https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[]}
def find_max_sum(nums1, nums2, k)
  n = nums1.length
  arr = (0...n).map { |i| [nums1[i], nums2[i], i] }
  arr.sort_by! { |x| x[0] }
  ans = Array.new(n, 0)
  h = []
  s = 0
  i = 0
  while i < n
    v = arr[i][0]
    start = i
    i += 1 while i < n && arr[i][0] == v
    (start...i).each { |t| ans[arr[t][2]] = s }
    (start...i).each do |t|
      h << arr[t][1]
      h.sort!
      s += arr[t][1]
      s -= h.shift if h.length > k
    end
  end
  ans
end
