# LeetCode 3641 - Longest Semi-Repeating Subarray
# https://leetcode.com/problems/longest-semi-repeating-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def longest_subarray(nums, k)
  cnt = Hash.new(0)
  ans = 0
  cur = 0
  l = 0
  nums.each_with_index do |x, r|
    c = cnt[x] + 1
    cnt[x] = c
    cur += 1 if c == 2
    while cur > k
      c2 = cnt[nums[l]] - 1
      cnt[nums[l]] = c2
      cur -= 1 if c2 == 1
      l += 1
    end
    ans = r - l + 1 if r - l + 1 > ans
  end
  ans
end
