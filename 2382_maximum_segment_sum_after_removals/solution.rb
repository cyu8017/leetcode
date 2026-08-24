# LeetCode 2382 - Maximum Segment Sum After Removals
# https://leetcode.com/problems/maximum-segment-sum-after-removals/

# @param {Integer[]} nums
# @param {Integer[]} remove_queries
# @return {Integer[]}
def maximum_segment_sum(nums, remove_queries)
  n = nums.length
  parent = (0...n).to_a
  ssum = Array.new(n, 0)
  active = Array.new(n, false)
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    parent[rb] = ra
    ssum[ra] += ssum[rb]
  end
  ans = Array.new(n, 0)
  best = 0
  (n - 1).downto(0) do |i|
    ans[i] = best
    idx = remove_queries[i]
    active[idx] = true
    ssum[idx] = nums[idx]
    unite.call(idx, idx - 1) if idx > 0 && active[idx - 1]
    unite.call(idx, idx + 1) if idx + 1 < n && active[idx + 1]
    cand = ssum[find.call(idx)]
    best = cand if cand > best
  end
  ans
end
