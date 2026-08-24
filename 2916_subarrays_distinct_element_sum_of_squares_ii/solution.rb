# LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
  mod = 1_000_000_007
  n = nums.length
  tree = Array.new(4 * (n + 2)) { { "sum" => 0, "sumSq" => 0, "lazy" => 0 } }

  apply = lambda do |idx, l, r, val|
    length = r - l + 1
    tree[idx]["sumSq"] = (
      tree[idx]["sumSq"] +
      2 * val % mod * tree[idx]["sum"] % mod +
      val % mod * val % mod * length % mod
    ) % mod
    tree[idx]["sum"] = (tree[idx]["sum"] + val % mod * length % mod) % mod
    tree[idx]["lazy"] = (tree[idx]["lazy"] + val) % mod
  end

  update = nil
  update = lambda do |idx, l, r, ql, qr, val|
    return if ql > r || qr < l
    if ql <= l && r <= qr
      apply.call(idx, l, r, val)
      return
    end
    if tree[idx]["lazy"] != 0 && l != r
      mid = (l + r) / 2
      apply.call(idx * 2, l, mid, tree[idx]["lazy"])
      apply.call(idx * 2 + 1, mid + 1, r, tree[idx]["lazy"])
      tree[idx]["lazy"] = 0
    end
    mid = (l + r) / 2
    update.call(idx * 2, l, mid, ql, qr, val)
    update.call(idx * 2 + 1, mid + 1, r, ql, qr, val)
    tree[idx]["sum"] = (tree[idx * 2]["sum"] + tree[idx * 2 + 1]["sum"]) % mod
    tree[idx]["sumSq"] = (tree[idx * 2]["sumSq"] + tree[idx * 2 + 1]["sumSq"]) % mod
  end

  last = {}
  ans = 0
  (1..n).each do |i|
    v = nums[i - 1]
    prev = last.fetch(v, 0)
    update.call(1, 1, n, prev + 1, i, 1)
    ans = (ans + tree[1]["sumSq"]) % mod
    last[v] = i
  end
  ans
end
