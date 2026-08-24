# LeetCode 3722 - Lexicographically Smallest String After Reverse
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

# @param {String} s
# @return {String}
def lex_smallest(s)
  ans = s
  n = s.length
  reverse = lambda do |a, l, r|
    i = l
    j = r - 1
    while i < j
      a[i], a[j] = a[j], a[i]
      i += 1
      j -= 1
    end
  end
  (1..n).each do |k|
    a1 = s.chars
    reverse.call(a1, 0, k)
    t1 = a1.join
    a2 = s.chars
    reverse.call(a2, n - k, n)
    t2 = a2.join
    ans = t1 if t1 < ans
    ans = t2 if t2 < ans
  end
  ans
end
