# LeetCode 3935 - Power Update After K Th Largest Insertion I
# https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

# @param {Integer[]} nums
# @param {Integer} p
# @param {Integer[][]} queries
# @return {Integer[]}
def power_update(nums, p, queries)
  merge = lambda do |st, x, v|
    c = st.fetch(x, 0)
    if c + v == 0
      st.delete(x)
    else
      st[x] = c + v
    end
  end
  first_key = lambda { |st| st.keys.min }
  last_key = lambda { |st| st.keys.max }
  qpow = lambda do |a, b, mod|
    ans = 1
    a = a.to_i
    while b > 0
      ans = (ans * a) % mod if (b & 1) != 0
      a = (a * a) % mod
      b >>= 1
    end
    ans
  end
  left = {}
  right = {}
  sz1 = 0
  sz2 = nums.length
  nums.each { |x| merge.call(right, x, 1) }
  mod = 1_000_000_007
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    val, k = q[0], q[1]
    merge.call(right, val, 1)
    sz2 += 1
    node = first_key.call(right)
    merge.call(right, node, -1)
    sz2 -= 1
    merge.call(left, node, 1)
    sz1 += 1
    while sz2 < k
      node = last_key.call(left)
      merge.call(left, node, -1)
      sz1 -= 1
      merge.call(right, node, 1)
      sz2 += 1
    end
    while sz2 > k
      node = first_key.call(right)
      merge.call(right, node, -1)
      sz2 -= 1
      merge.call(left, node, 1)
      sz1 += 1
    end
    x = first_key.call(right)
    p = qpow.call(p, x, mod)
    ans[qi] = p
  end
  ans
end
