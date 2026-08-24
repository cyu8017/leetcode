# LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

# @param {String} s
# @param {String} target
# @return {String}
def lex_palindromic_permutation(s, target)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  odd = 0
  mid = -1
  (0...26).each do |i|
    if cnt[i].odd?
      odd += 1
      mid = i
    end
  end
  return "" if odd > 1
  half = (0...26).map { |i| cnt[i] / 2 }
  n = s.length
  half_len = n / 2
  left = Array.new(half_len, "")
  dfs = nil
  dfs = lambda do |pos, greater|
    if pos == half_len
      return greater if mid < 0
      return true if greater
      return (97 + mid).chr > target[half_len]
    end
    start = greater ? 0 : (target[pos].ord - 97)
    (start...26).each do |c|
      next if half[c] == 0
      half[c] -= 1
      left[pos] = (97 + c).chr
      return true if dfs.call(pos + 1, greater || c > (target[pos].ord - 97))
      half[c] += 1
    end
    false
  end
  return "" unless dfs.call(0, false)
  res = left.join
  res += (97 + mid).chr if mid >= 0
  (half_len - 1).downto(0) { |i| res += left[i] }
  return "" if res <= target
  res
end
