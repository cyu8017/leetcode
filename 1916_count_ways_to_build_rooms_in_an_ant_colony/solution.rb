# LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
# https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

# @param {Integer[]} prev_room
# @return {Integer}
def ways_to_build_rooms(prev_room)
  mod = 10**9 + 7
  n = prev_room.length
  children = Array.new(n) { [] }
  prev_room.each_with_index do |prev, room|
    children[prev] << room if prev != -1
  end
  fact = Array.new(n + 1, 1)
  inv_fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_fact[n] = mod_pow(fact[n], mod - 2, mod)
  n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % mod }

  comb = ->(a, b) { fact[a] * inv_fact[b] % mod * inv_fact[a - b] % mod }

  dfs = lambda do |node|
    size = 0
    ways = 1
    children[node].each do |child|
      child_size, child_ways = dfs.call(child)
      ways = ways * child_ways % mod * comb.call(size + child_size, child_size) % mod
      size += child_size
    end
    [size + 1, ways]
  end

  dfs.call(0)[1]
end

def mod_pow(base, exp, mod)
  result = 1
  base %= mod
  while exp.positive?
    result = result * base % mod if exp.odd?
    base = base * base % mod
    exp /= 2
  end
  result
end
