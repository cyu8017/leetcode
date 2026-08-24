# LeetCode 2070 - Most Beautiful Item for Each Query
# https://leetcode.com/problems/most-beautiful-item-for-each-query/

# @param {Integer[][]} items
# @param {Integer[]} queries
# @return {Integer[]}
def maximum_beauty(items, queries)
  items.sort_by! { |it| it[0] }
  max_b = 0
  items.each do |it|
    max_b = [max_b, it[1]].max
    it[1] = max_b
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    lo = 0
    hi = items.length
    while lo < hi
      mid = (lo + hi) >> 1
      if items[mid][0] <= q
        lo = mid + 1
      else
        hi = mid
      end
    end
    ans[i] = lo.zero? ? 0 : items[lo - 1][1]
  end
  ans
end
