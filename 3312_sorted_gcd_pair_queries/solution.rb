# LeetCode 3312 - Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def gcd_values(nums, queries)
  max_v = nums.max
  cnt = Array.new(max_v + 1, 0)
  nums.each { |x| cnt[x] += 1 }
  div_cnt = Array.new(max_v + 1, 0)
  (1..max_v).each do |g|
    c = 0
    m = g
    while m <= max_v
      c += cnt[m]
      m += g
    end
    div_cnt[g] = c * (c - 1) / 2
  end
  exact = Array.new(max_v + 1, 0)
  max_v.downto(1) do |g|
    exact[g] = div_cnt[g]
    m = 2 * g
    while m <= max_v
      exact[g] -= exact[m]
      m += g
    end
  end
  pref = Array.new(max_v + 1, 0)
  (1..max_v).each { |g| pref[g] = pref[g - 1] + exact[g] }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    lo = 1
    hi = max_v
    while lo < hi
      mid = (lo + hi) >> 1
      if pref[mid] > q
        hi = mid
      else
        lo = mid + 1
      end
    end
    ans[i] = lo
  end
  ans
end
