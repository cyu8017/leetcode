# LeetCode 2800 - Shortest String That Contains Three Strings
# https://leetcode.com/problems/shortest-string-that-contains-three-strings/

# @param {String} a
# @param {String} b
# @param {String} c
# @return {String}
def minimum_string(a, b, c)
  merge = lambda do |x, y|
    return x if x.include?(y)
    best = x + y
    n = [x.length, y.length].min
    n.downto(1) do |i|
      if x[-i..] == y[0, i]
        cand = x + y[i..]
        best = cand if cand.length < best.length || (cand.length == best.length && cand < best)
        break
      end
    end
    best
  end
  perms = [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]
  ans = ""
  perms.each do |p|
    cur = merge.call(merge.call(p[0], p[1]), p[2])
    ans = cur if ans.empty? || cur.length < ans.length || (cur.length == ans.length && cur < ans)
  end
  ans
end
