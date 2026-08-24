# LeetCode 3930 - Power Update After K Th Largest Insertion Ii
# https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

# @param {Integer[]} nums
# @param {Integer} p
# @param {Integer[][]} queries
# @return {Integer[]}
def power_update(nums, p, queries)
  sl = nums.sort
  mod = 10**9 + 7
  ans = []
  queries.each do |val, k|
    lo = 0
    hi = sl.length
    while lo < hi
      mid = (lo + hi) / 2
      if sl[mid] < val
        lo = mid + 1
      else
        hi = mid
      end
    end
    sl.insert(lo, val)
    exp = sl[-k]
    p = p.to_i.pow(exp, mod)
    ans << p
  end
  ans
end
