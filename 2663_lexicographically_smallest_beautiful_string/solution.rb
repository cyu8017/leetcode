# LeetCode 2663 - Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def smallest_beautiful_string(s, k)
  n = s.length
  b = s.chars
  (n - 1).downto(0) do |i|
    ((b[i].ord + 1)...(97 + k)).each do |code|
      c = code.chr
      next if (i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2])

      b[i] = c
      ((i + 1)...n).each do |j|
        (97...(97 + k)).each do |nc|
          ch = nc.chr
          next if (j > 0 && ch == b[j - 1]) || (j > 1 && ch == b[j - 2])

          b[j] = ch
          break
        end
      end
      return b.join
    end
  end
  ""
end
