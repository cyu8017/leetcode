# LeetCode 2698 - Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

# @param {Integer} n
# @return {Integer}
def punishment_number(n)
  dfs = nil
  dfs = lambda do |s, i, sm, target|
    return sm == target if i == s.length

    cur = 0
    (i...s.length).each do |j|
      cur = cur * 10 + (s[j].ord - 48)
      break if sm + cur > target
      return true if dfs.call(s, j + 1, sm + cur, target)
    end
    false
  end
  ans = 0
  (1..n).each do |i|
    sq = i * i
    ans += sq if dfs.call(sq.to_s, 0, 0, i)
  end
  ans
end
