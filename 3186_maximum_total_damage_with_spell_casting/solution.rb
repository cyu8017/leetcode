# LeetCode 3186 - Maximum Total Damage With Spell Casting
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

# @param {Integer[]} power
# @return {Integer}
def maximum_total_damage(power)
  n = power.length
  power.sort!
  cnt = Hash.new(0)
  nxt = Array.new(n, 0)
  f = Array.new(n, 0)
  (0...n).each do |i|
    cnt[power[i]] += 1
    nxt[i] = power.bsearch_index { |v| v >= power[i] + 3 } || n
  end
  dfs = lambda do |i|
    return 0 if i >= n
    return f[i] if f[i] != 0
    a = dfs.call(i + cnt[power[i]])
    b = power[i] * cnt[power[i]] + dfs.call(nxt[i])
    f[i] = [a, b].max
  end
  dfs.call(0)
end
