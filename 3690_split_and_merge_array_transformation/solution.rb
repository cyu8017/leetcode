# LeetCode 3690 - Split and Merge Array Transformation
# https://leetcode.com/problems/split-and-merge-array-transformation/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_split_merge(nums1, nums2)
  n = nums1.length
  to_arr = lambda do |nums|
    t = Array.new(6, 0)
    (0...n).each { |i| t[i] = nums[i] }
    t
  end
  start = to_arr.call(nums1)
  target = to_arr.call(nums2)
  vis = { start => true }
  q = [start]
  ans = 0
  loop do
    nq = []
    q.each do |cur|
      return ans if cur == target

      (0...n).each do |l|
        (l...n).each do |r|
          remain = cur[0...l] + cur[(r + 1)...n]
          sub = cur[l..r]
          (0..remain.length).each do |pos|
            nxt_slice = remain[0...pos] + sub + remain[pos..-1]
            nxt = to_arr.call(nxt_slice)
            unless vis[nxt]
              vis[nxt] = true
              nq << nxt
            end
          end
        end
      end
    end
    q = nq
    ans += 1
  end
end
