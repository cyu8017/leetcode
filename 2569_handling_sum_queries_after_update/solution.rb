# LeetCode 2569 - Handling Sum Queries After Update
# https://leetcode.com/problems/handling-sum-queries-after-update/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def handle_query(nums1, nums2, queries)
  n = nums1.length
  ones = Array.new(4 * n, 0)
  lazy = Array.new(4 * n, false)

  build = nil
  build = lambda do |idx, l, r|
    if l == r
      ones[idx] = nums1[l]
      return
    end
    m = (l + r) >> 1
    build.call(idx * 2, l, m)
    build.call(idx * 2 + 1, m + 1, r)
    ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
  end

  apply = lambda do |idx, l, r|
    ones[idx] = (r - l + 1) - ones[idx]
    lazy[idx] = !lazy[idx]
  end

  push = lambda do |idx, l, r|
    if lazy[idx] && l != r
      m = (l + r) >> 1
      apply.call(idx * 2, l, m)
      apply.call(idx * 2 + 1, m + 1, r)
      lazy[idx] = false
    end
  end

  update = nil
  update = lambda do |idx, l, r, ql, qr|
    if ql <= l && r <= qr
      apply.call(idx, l, r)
      return
    end
    push.call(idx, l, r)
    m = (l + r) >> 1
    update.call(idx * 2, l, m, ql, qr) if ql <= m
    update.call(idx * 2 + 1, m + 1, r, ql, qr) if qr > m
    ones[idx] = ones[idx * 2] + ones[idx * 2 + 1]
  end

  build.call(1, 0, n - 1)
  sum2 = nums2.sum
  ans = []
  queries.each do |q|
    if q[0] == 1
      update.call(1, 0, n - 1, q[1], q[2])
    elsif q[0] == 2
      sum2 += q[1] * ones[1]
    else
      ans << sum2
    end
  end
  ans
end
