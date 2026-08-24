# LeetCode 2156 - Find Substring With Given Hash Value
# https://leetcode.com/problems/find-substring-with-given-hash-value/

# @param {String} s
# @param {Integer} power
# @param {Integer} modulo
# @param {Integer} k
# @param {Integer} hash_value
# @return {String}
def sub_str_hash(s, power, modulo, k, hash_value)
  n = s.length
  pk = 1
  (k - 1).times { pk = pk * power % modulo }
  h = 0
  ans = 0
  (n - 1).downto(n - k) do |i|
    h = (h * power + (s[i].ord - 96)) % modulo
  end
  ans = n - k if h == hash_value
  (n - k - 1).downto(0) do |i|
    h = (h - (s[i + k].ord - 96) * pk % modulo + modulo) % modulo
    h = (h * power + (s[i].ord - 96)) % modulo
    ans = i if h == hash_value
  end
  s[ans, k]
end
