# LeetCode 3455 - Shortest Matching Substring
# https://leetcode.com/problems/shortest-matching-substring/

# @param {String} s
# @param {String} p
# @return {Integer}
def shortest_matching_substring(s, p)
  parts = []
  cur = ""
  p.each_char do |c|
    if c == "*"
      parts << cur
      cur = ""
    else
      cur += c
    end
  end
  parts << cur
  parts << "" while parts.length < 3
  a = parts[0]
  b = parts[1]
  c = parts[2]
  n = s.length
  find_all = lambda do |sub|
    res = []
    if sub.length == 0
      (0..n).each { |i| res << i }
      return res
    end
    (0..(n - sub.length)).each do |i|
      res << i if s[i, sub.length] == sub
    end
    res
  end
  sort_search = lambda do |arr, x|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  pos_a = find_all.call(a)
  pos_b = find_all.call(b)
  pos_c = find_all.call(c)
  ans = n + 1
  pos_a.each do |ia|
    end_a = ia + a.length
    bi = sort_search.call(pos_b, end_a)
    while bi < pos_b.length
      end_b = pos_b[bi] + b.length
      ci = sort_search.call(pos_c, end_b)
      if ci < pos_c.length
        length = pos_c[ci] + c.length - ia
        ans = length if length < ans
      end
      break
    end
  end
  ans == n + 1 ? -1 : ans
end
