# LeetCode 3569 - Maximize Count of Distinct Primes After Split
# https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_count(nums, queries)
  mx = nums.max
  queries.each { |q| mx = [mx, q[1]].max }
  is_p = Array.new(mx + 1, false)
  (2..mx).each { |i| is_p[i] = true }
  i = 2
  while i * i <= mx
    if is_p[i]
      (i * i).step(mx, i) { |j| is_p[j] = false }
    end
    i += 1
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    nums[q[0]] = q[1]
    best = 0
    left = {}
    right = {}
    nums.each do |v|
      right[v] = (right[v] || 0) + 1 if v <= mx && is_p[v]
    end
    (0...(nums.length - 1)).each do |ii|
      v = nums[ii]
      if v <= mx && is_p[v]
        left[v] = (left[v] || 0) + 1
        c = right[v] - 1
        if c == 0
          right.delete(v)
        else
          right[v] = c
        end
      end
      best = [best, left.length + right.length].max
    end
    ans[qi] = best
  end
  ans
end
