# LeetCode 3735 - Lexicographically Smallest String After Reverse II
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

# @param {String} s
# @return {String}
def lex_smallest(s)
  n = s.length
  best = s
  reverse = lambda do |a, l, r|
    i = l
    j = r - 1
    while i < j
      a[i], a[j] = a[j], a[i]
      i += 1
      j -= 1
    end
  end
  (1..n).each do |i|
    t = s.chars
    reverse.call(t, 0, i)
    ts = t.join
    best = ts if ts < best
  end
  (0...n).each do |i|
    t = s.chars
    reverse.call(t, i, n)
    ts = t.join
    best = ts if ts < best
  end
  best
end
