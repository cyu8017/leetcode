# LeetCode 2287 - Rearrange Characters to Make Target String
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

# @param {String} s
# @param {String} target
# @return {Integer}
def rearrange_characters(s, target)
  sc = Array.new(26, 0)
  tc = Array.new(26, 0)
  s.each_char { |c| sc[c.ord - 97] += 1 }
  target.each_char { |c| tc[c.ord - 97] += 1 }
  ans = Float::INFINITY
  26.times do |i|
    next if tc[i] == 0

    ans = [ans, sc[i] / tc[i]].min
  end
  ans.to_i
end
