# LeetCode 3526 - Range XOR Queries with Subarray Reversals
# https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def get_results(nums, queries)
  a = nums.dup
  ans = []
  at = lambda { |i| (i >= 0 && i < a.length) ? a[i] : 0 }
  set_at = lambda do |i, val|
    return if i < 0
    a << 0 while a.length <= i
    a[i] = val
  end
  queries.each do |q|
    typ = q[0]
    if typ == 1
      l = q[1]
      r = q[2]
      while l < r
        left = at.call(l)
        right = at.call(r)
        set_at.call(l, right)
        set_at.call(r, left)
        l += 1
        r -= 1
      end
    elsif typ == 2
      x = 0
      (q[1]..q[2]).each { |i| x ^= at.call(i) }
      ans << x
    else
      set_at.call(q[1], q[2])
    end
  end
  ans
end
