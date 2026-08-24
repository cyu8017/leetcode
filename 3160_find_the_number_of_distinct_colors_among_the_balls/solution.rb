# LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

# @param {Integer} limit
# @param {Integer[][]} queries
# @return {Integer[]}
def query_results(limit, queries)
  g = {}
  cnt = {}
  queries.map do |q|
    x = q[0]
    y = q[1]
    cnt[y] = cnt.fetch(y, 0) + 1
    old = g[x]
    unless old.nil?
      nv = cnt[old] - 1
      if nv == 0
        cnt.delete(old)
      else
        cnt[old] = nv
      end
    end
    g[x] = y
    cnt.length
  end
end
