# LeetCode 3209 - Number of Subarrays With AND Value of K
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  pre = {}
  ans = 0
  nums.each do |x|
    cur = {}
    pre.each do |key, val|
      nk = x & key
      cur[nk] = cur.fetch(nk, 0) + val
    end
    cur[x] = cur.fetch(x, 0) + 1
    ans += cur.fetch(k, 0)
    pre = cur
  end
  ans
end
