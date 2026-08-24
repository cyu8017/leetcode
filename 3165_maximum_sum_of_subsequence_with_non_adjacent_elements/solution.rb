# LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class Node
  attr_accessor :l, :r, :s00, :s01, :s10, :s11
  def initialize
    @l = 0
    @r = 0
    @s00 = 0
    @s01 = 0
    @s10 = 0
    @s11 = 0
  end
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def maximum_sum_subsequence(nums, queries)
  n = nums.length
  tr = Array.new(n * 4) { Node.new }

  build = nil
  build = lambda do |u, l, r|
    tr[u].l = l
    tr[u].r = r
    return if l == r
    mid = (l + r) >> 1
    build.call(u << 1, l, mid)
    build.call(u << 1 | 1, mid + 1, r)
  end

  pushup = lambda do |u|
    left = tr[u << 1]
    right = tr[u << 1 | 1]
    tr[u].s00 = [left.s00 + right.s10, left.s01 + right.s00].max
    tr[u].s01 = [left.s00 + right.s11, left.s01 + right.s01].max
    tr[u].s10 = [left.s10 + right.s10, left.s11 + right.s00].max
    tr[u].s11 = [left.s10 + right.s11, left.s11 + right.s01].max
  end

  modify = nil
  modify = lambda do |u, x, v|
    if tr[u].l == tr[u].r
      tr[u].s11 = [0, v].max
      return
    end
    mid = (tr[u].l + tr[u].r) >> 1
    if x <= mid
      modify.call(u << 1, x, v)
    else
      modify.call(u << 1 | 1, x, v)
    end
    pushup.call(u)
  end

  query = nil
  query = lambda do |u, l, r|
    return tr[u].s11 if tr[u].l >= l && tr[u].r <= r
    mid = (tr[u].l + tr[u].r) >> 1
    ans = 0
    ans = query.call(u << 1, l, r) if r <= mid
    ans = [ans, query.call(u << 1 | 1, l, r)].max if l > mid
    ans
  end

  build.call(1, 1, n)
  n.times { |i| modify.call(1, i + 1, nums[i]) }
  mod = 1_000_000_007
  ans = 0
  queries.each do |q|
    modify.call(1, q[0] + 1, q[1])
    ans = (ans + query.call(1, 1, n)) % mod
  end
  ans
end
