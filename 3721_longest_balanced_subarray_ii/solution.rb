# LeetCode 3721 - Longest Balanced Subarray II
# https://leetcode.com/problems/longest-balanced-subarray-ii/

class LbNode
  attr_accessor :l, :r, :mn, :mx, :lazy

  def initialize
    @l = 0
    @r = 0
    @mn = 0
    @mx = 0
    @lazy = 0
  end
end

class LbSegmentTree
  def initialize(n)
    @tr = Array.new(n << 2) { LbNode.new }
    build(1, 0, n)
  end

  def build(u, l, r)
    tr = @tr
    tr[u].l = l
    tr[u].r = r
    tr[u].mn = 0
    tr[u].mx = 0
    tr[u].lazy = 0
    return if l == r
    mid = (l + r) >> 1
    build(u << 1, l, mid)
    build((u << 1) | 1, mid + 1, r)
  end

  def apply(u, v)
    @tr[u].mn += v
    @tr[u].mx += v
    @tr[u].lazy += v
  end

  def pushup(u)
    tr = @tr
    tr[u].mn = [tr[u << 1].mn, tr[(u << 1) | 1].mn].min
    tr[u].mx = [tr[u << 1].mx, tr[(u << 1) | 1].mx].max
  end

  def pushdown(u)
    if @tr[u].lazy != 0
      v = @tr[u].lazy
      apply(u << 1, v)
      apply((u << 1) | 1, v)
      @tr[u].lazy = 0
    end
  end

  def modify(u, l, r, v)
    tr = @tr
    if tr[u].l >= l && tr[u].r <= r
      apply(u, v)
      return
    end
    pushdown(u)
    mid = (tr[u].l + tr[u].r) >> 1
    modify(u << 1, l, r, v) if l <= mid
    modify((u << 1) | 1, l, r, v) if r > mid
    pushup(u)
  end

  def query(u, target)
    tr = @tr
    return tr[u].l if tr[u].l == tr[u].r
    pushdown(u)
    left = u << 1
    right = (u << 1) | 1
    return query(left, target) if tr[left].mn <= target && target <= tr[left].mx
    query(right, target)
  end
end

# @param {Integer[]} nums
# @return {Integer}
def longest_balanced(nums)
  n = nums.length
  st = LbSegmentTree.new(n)
  last = {}
  now = 0
  ans = 0
  (1..n).each do |i|
    x = nums[i - 1]
    det = (x & 1) != 0 ? 1 : -1
    if last.key?(x)
      st.modify(1, last[x], n, -det)
      now -= det
    end
    last[x] = i
    st.modify(1, i, n, det)
    now += det
    pos = st.query(1, now)
    ans = [ans, i - pos].max
  end
  ans
end
