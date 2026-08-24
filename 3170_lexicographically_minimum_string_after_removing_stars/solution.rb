# LeetCode 3170 - Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

# @param {String} s
# @return {String}
def clear_stars(s)
  g = Array.new(26) { [] }
  n = s.length
  rem = Array.new(n, false)
  s.each_char.with_index do |ch, i|
    if ch == "*"
      rem[i] = true
      26.times do |j|
        if !g[j].empty?
          rem[g[j].pop] = true
          break
        end
      end
    else
      g[ch.ord - 97] << i
    end
  end
  n.times.select { |i| !rem[i] }.map { |i| s[i] }.join
end
