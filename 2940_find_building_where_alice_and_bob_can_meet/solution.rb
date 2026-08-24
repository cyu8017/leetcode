# LeetCode 2940 - Find Building Where Alice and Bob Can Meet
# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

# @param {Integer[]} heights
# @param {Integer[][]} queries
# @return {Integer[]}
def leftmost_building_queries(heights, queries)
  qn = queries.length
  ans = Array.new(qn, -1)
  buckets = Array.new(heights.length) { [] }
  qn.times do |qi|
    a = queries[qi][0]
    b = queries[qi][1]
    a, b = b, a if a > b
    if a == b || heights[a] < heights[b]
      ans[qi] = b
      next
    end
    buckets[b] << [heights[a], qi]
  end
  st = []
  (heights.length - 1).downto(0) do |i|
    buckets[i].each do |h, qi|
      lo = 0
      hi = st.length - 1
      pos = -1
      while lo <= hi
        mid = (lo + hi) / 2
        if st[mid][0] > h
          pos = st[mid][1]
          lo = mid + 1
        else
          hi = mid - 1
        end
      end
      ans[qi] = pos
    end
    st.pop while !st.empty? && st[-1][0] <= heights[i]
    st << [heights[i], i]
  end
  ans
end
