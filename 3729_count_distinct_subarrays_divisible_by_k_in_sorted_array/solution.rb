# LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
# https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def num_good_subarrays(nums, k)
  ans = 0
  s = 0
  cnt = Hash.new(0)
  cnt[0] = 1
  nums.each do |x|
    s = (s + x) % k
    ans += cnt[s]
    cnt[s] += 1
  end
  n = nums.length
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && nums[j] == nums[i]
    m = j - i
    (1..m).each do |h|
      ans -= m - h if (nums[i] * h) % k == 0
    end
    i = j
  end
  ans
end
