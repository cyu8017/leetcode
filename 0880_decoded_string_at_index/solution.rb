# LeetCode 0880 - Decoded String at Index
# https://leetcode.com/problems/decoded-string-at-index/

# @param {String} s
# @param {Integer} k
# @return {String}
def decode_at_index(s, k)
  size = 0
  s.each_char do |ch|
    if ch =~ /\d/
      size *= ch.to_i
    else
      size += 1
    end
  end
  s.reverse.each_char do |ch|
    k %= size
    return ch if k == 0 && ch =~ /[A-Za-z]/
    if ch =~ /\d/
      size /= ch.to_i
    else
      size -= 1
    end
  end
  ""
end
