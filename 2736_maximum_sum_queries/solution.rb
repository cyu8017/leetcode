# LeetCode 2736 - Maximum Sum Queries
# https://leetcode.com/problems/maximum-sum-queries/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def maximum_sum_queries(nums1, nums2, queries)
  n = nums1.length
  pts = (0...n).map { |i| [nums1[i], nums2[i], nums1[i] + nums2[i]] }
  pts.sort_by! { |p| -p[0] }
  qs = queries.each_with_index.map { |q, i| [q[0], q[1], i] }
  qs.sort_by! { |q| -q[0] }
  ys = (nums2 + qs.map { |q| q[1] }).sort
  uniq = []
  ys.each { |y| uniq << y if uniq.empty? || uniq[-1] != y }
  m = uniq.length
  bit = Array.new(m + 2, -1)

  rank = lambda do |y|
    lo = 0
    hi = m
    while lo < hi
      mid = (lo + hi) >> 1
      if uniq[mid] < y
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo + 1
  end

  update = lambda do |i, v|
    while i <= m
      bit[i] = v if v > bit[i]
      i += i & -i
    end
  end

  query = lambda do |i|
    best = -1
    while i > 0
      best = bit[i] if bit[i] > best
      i -= i & -i
    end
    best
  end

  ans = Array.new(queries.length, 0)
  j = 0
  qs.each do |q|
    while j < n && pts[j][0] >= q[0]
      update.call(m - rank.call(pts[j][1]) + 1, pts[j][2])
      j += 1
    end
    ans[q[2]] = query.call(m - rank.call(q[1]) + 1)
  end
  ans
end
