# LeetCode 3097 - Shortest Subarray With OR at Least K II
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_subarray_length(nums, k)
  n = nums.length
  cnt = Array.new(32, 0)
  ans = n + 1
  s = 0
  i = 0
  n.times do |j|
    x = nums[j]
    s |= x
    32.times { |h| cnt[h] += 1 if ((x >> h) & 1) != 0 }
    while s >= k && i <= j
      ans = [ans, j - i + 1].min
      32.times do |h|
        if ((nums[i] >> h) & 1) != 0
          cnt[h] -= 1
          s ^= 1 << h if cnt[h] == 0
        end
      end
      i += 1
    end
  end
  ans == n + 1 ? -1 : ans
end
