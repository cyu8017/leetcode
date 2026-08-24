# LeetCode 2845 - Count of Interesting Subarrays
# https://leetcode.com/problems/count-of-interesting-subarrays/

# @param {Integer[]} nums
# @param {Integer} modulo
# @param {Integer} k
# @return {Integer}
def count_interesting_subarrays(nums, modulo, k)
  freq = { 0 => 1 }
  ans = 0
  pref = 0
  nums.each do |v|
    pref += 1 if v % modulo == k
    need = (pref - k) % modulo
    need += modulo if need < 0
    ans += freq.fetch(need, 0)
    key = pref % modulo
    freq[key] = freq.fetch(key, 0) + 1
  end
  ans
end
