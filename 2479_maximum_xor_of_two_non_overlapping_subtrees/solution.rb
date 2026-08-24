# LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
# https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} values
# @return {Integer}
def max_xor(n, edges, values)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  subtree = Array.new(n, 0)

  dfs_sum = lambda do |u, p|
    s = values[u]
    g[u].each { |v| s += dfs_sum.call(v, u) if v != p }
    subtree[u] = s
    s
  end
  dfs_sum.call(0, -1)

  root = { "child" => [nil, nil] }

  insert = lambda do |x|
    cur = root
    46.downto(0) do |b|
      bit = (x >> b) & 1
      cur["child"][bit] = { "child" => [nil, nil] } if cur["child"][bit].nil?
      cur = cur["child"][bit]
    end
  end

  query = lambda do |x|
    cur = root
    return 0 if cur["child"][0].nil? && cur["child"][1].nil?

    res = 0
    46.downto(0) do |b|
      bit = (x >> b) & 1
      want = bit ^ 1
      if cur["child"][want]
        res |= 1 << b
        cur = cur["child"][want]
      elsif cur["child"][bit]
        cur = cur["child"][bit]
      else
        return res
      end
    end
    res
  end

  ans = [0]
  dfs = lambda do |u, p|
    g[u].each do |v|
      next if v == p

      xorv = query.call(subtree[v])
      ans[0] = xorv if xorv > ans[0]
      dfs.call(v, u)
      insert.call(subtree[v])
    end
  end
  dfs.call(0, -1)
  ans[0]
end
