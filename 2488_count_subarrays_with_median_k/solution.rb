# LeetCode 2488 - Count Subarrays With Median K
# https://leetcode.com/problems/count-subarrays-with-median-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  pos = 0
  nums.each_with_index do |x, i|
    if x == k
      pos = i
      break
    end
  end
  bal = Hash.new(0)
  bal[0] = 1
  cur = 0
  (pos - 1).downto(0) do |i|
    cur += nums[i] < k ? -1 : 1
    bal[cur] += 1
  end
  ans = bal[0] + bal[1]
  cur = 0
  ((pos + 1)...nums.length).each do |i|
    cur += nums[i] < k ? -1 : 1
    ans += bal[-cur] + bal[1 - cur]
  end
  ans
end
