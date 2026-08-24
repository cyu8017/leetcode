# LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def popcount_depth(nums, queries)
  bit_count = lambda do |x|
    c = 0
    v = x
    while v > 0
      c += v & 1
      v >>= 1
    end
    c
  end
  depth = lambda do |x|
    v = x
    return 0 if v == 1

    d = 0
    while v > 1
      v = bit_count.call(v)
      d += 1
    end
    d
  end
  a = nums.dup
  ans = []
  queries.each do |q|
    if q[0] == 1
      l, r, k = q[1], q[2], q[3]
      cnt = 0
      (l..r).each { |i| cnt += 1 if depth.call(a[i]) == k }
      ans << cnt
    else
      a[q[1]] = q[2]
    end
  end
  ans
end
