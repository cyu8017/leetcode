# LeetCode 3490 - Count Beautiful Numbers
# https://leetcode.com/problems/count-beautiful-numbers/

# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def beautiful_numbers(l, r)
  count_beautiful_3490(r) - count_beautiful_3490(l - 1)
end

def count_beautiful_3490(n)
  return 0 if n <= 0

  s = n.to_s
  dfs = nil
  dfs = lambda do |pos, tight, sm, prod, started|
    if pos == s.length
      return 0 unless started
      return sm > 0 && prod % sm == 0 ? 1 : 0
    end
    up = tight ? s[pos].ord - 48 : 9
    ans = 0
    (0..up).each do |d|
      nt = tight && d == up
      ans += if !started && d == 0
               dfs.call(pos + 1, nt, 0, 1, false)
             else
               ns = sm + d
               np = started ? prod * d : d
               dfs.call(pos + 1, nt, ns, np, true)
             end
    end
    ans
  end
  dfs.call(0, true, 0, 1, false)
end
