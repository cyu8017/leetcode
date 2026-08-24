# LeetCode 3271 - Hash Divided String
# https://leetcode.com/problems/hash-divided-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def string_hash(s, k)
  out = []
  (0...s.length).step(k) do |i|
    ssum = 0
    (i...(i + k)).each { |j| ssum += s[j].ord - 97 }
    out << (97 + ssum % 26).chr
  end
  out.join
end
