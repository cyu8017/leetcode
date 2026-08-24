# LeetCode 2407 - Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def length_of_lis(nums, k)
  max_v = nums.max
  tree = Array.new(4 * (max_v + 1), 0)
  update = nil
  query = nil
  update = lambda do |idx, l, r, pos, val|
    if l == r
      tree[idx] = val if val > tree[idx]
      return
    end
    mid = (l + r) >> 1
    if pos <= mid
      update.call(idx * 2, l, mid, pos, val)
    else
      update.call(idx * 2 + 1, mid + 1, r, pos, val)
    end
    tree[idx] = [tree[idx * 2], tree[idx * 2 + 1]].max
  end
  query = lambda do |idx, l, r, ql, qr|
    return 0 if qr < l || r < ql
    return tree[idx] if ql <= l && r <= qr
    mid = (l + r) >> 1
    [query.call(idx * 2, l, mid, ql, qr), query.call(idx * 2 + 1, mid + 1, r, ql, qr)].max
  end
  ans = 0
  nums.each do |x|
    lo = [1, x - k].max
    best = 1
    best = query.call(1, 1, max_v, lo, x - 1) + 1 if lo <= x - 1
    update.call(1, 1, max_v, x, best)
    ans = best if best > ans
  end
  ans
end
