# LeetCode 3161 - Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/

class FenwickMax
  def initialize(n)
    @vals = Array.new(n + 1, 0)
  end

  def maximize(i, val)
    while i < @vals.length
      @vals[i] = [@vals[i], val].max
      i += i & -i
    end
  end

  def get(i)
    res = 0
    while i > 0
      res = [res, @vals[i]].max
      i -= i & -i
    end
    res
  end
end

# @param {Integer[][]} queries
# @return {Boolean[]}
def get_results(queries)
  n = queries.length * 3
  n = 50_000 if n > 50_000
  tree = FenwickMax.new(n + 1)
  obs = [0, n]
  queries.each do |q|
    next unless q[0] == 1
    x = q[1]
    idx = bisect_left(obs, x)
    obs.insert(idx, x) if idx == obs.length || obs[idx] != x
  end
  (0...obs.length - 1).each { |i| tree.maximize(obs[i + 1], obs[i + 1] - obs[i]) }
  ans = []
  (queries.length - 1).downto(0) do |i|
    typ = queries[i][0]
    x = queries[i][1]
    if typ == 1
      j = bisect_left(obs, x)
      prev = obs[j - 1]
      nxt = obs[j + 1]
      obs.delete_at(j)
      tree.maximize(nxt, nxt - prev)
    else
      sz = queries[i][2]
      j = bisect_left(obs, x + 1) - 1
      prev = obs[j]
      ans << (tree.get(prev) >= sz || x - prev >= sz)
    end
  end
  ans.reverse
end

def bisect_left(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) / 2
    if a[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end
