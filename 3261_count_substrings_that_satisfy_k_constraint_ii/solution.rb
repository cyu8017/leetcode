# LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

# @param {String} s
# @param {Integer} k
# @param {Integer[][]} queries
# @return {Integer[]}
def count_k_constraint_substrings(s, k, queries)
  n = s.length
  left_most = Array.new(n, 0)
  z = o = l = 0
  (0...n).each do |r|
    if s[r] == "0"
      z += 1
    else
      o += 1
    end
    while z > k && o > k
      if s[l] == "0"
        z -= 1
      else
        o -= 1
      end
      l += 1
    end
    left_most[r] = l
  end
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + (i - left_most[i] + 1) }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    ll = q[0]
    rr = q[1]
    lo = ll
    hi = rr + 1
    while lo < hi
      mid = (lo + hi) >> 1
      if left_most[mid] < ll
        lo = mid + 1
      else
        hi = mid
      end
    end
    res = 0
    if lo > ll
      m = lo - ll
      res += m * (m + 1) / 2
    end
    res += pref[rr + 1] - pref[lo] if lo <= rr
    ans[qi] = res
  end
  ans
end
