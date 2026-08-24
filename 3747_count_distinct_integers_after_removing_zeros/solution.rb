# LeetCode 3747 - Count Distinct Integers After Removing Zeros
# https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

# @param {Integer} n
# @return {Integer}
def count_distinct(n)
  s = n.to_s
  m = s.length
  f = Array.new(20) { Array.new(2) { Array.new(2) { Array.new(2, -1) } } }
  dfs = nil
  dfs = lambda do |i, zero, lead, limit|
    if i == m
      return (zero == 0 && lead == 0) ? 1 : 0
    end
    return f[i][zero][lead][limit] if limit == 0 && f[i][zero][lead][limit] != -1
    up = limit == 1 ? (s[i].ord - 48) : 9
    ans = 0
    (0..up).each do |d|
      nxt_zero = zero
      nxt_zero = 1 if d == 0 && lead == 0
      nxt_lead = (lead == 1 && d == 0) ? 1 : 0
      nxt_limit = (limit == 1 && d == up) ? 1 : 0
      ans += dfs.call(i + 1, nxt_zero, nxt_lead, nxt_limit)
    end
    f[i][zero][lead][limit] = ans if limit == 0
    ans
  end
  dfs.call(0, 0, 1, 1)
end
