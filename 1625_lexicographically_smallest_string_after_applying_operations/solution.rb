# LeetCode 1625 - Lexicographically Smallest String After Applying Operations
# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

# @param {String} s
# @param {Integer} a
# @param {Integer} b
# @return {String}
def find_lex_smallest_string(s, a, b)
  seen = { s => true }
  q = [s]
  ans = s
  q.each do |cur|
    ans = [ans, cur].min
    add = cur.chars.each_with_index.map { |ch, i| ((ch.to_i + (i.odd? ? a : 0)) % 10).to_s }.join
    rot = cur[-b..] + cur[0...-b]
    [add, rot].each do |nxt|
      next if seen[nxt]

      seen[nxt] = true
      q << nxt
    end
  end
  ans
end
