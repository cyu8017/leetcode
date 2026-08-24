# LeetCode 2309 - Greatest English Letter in Upper and Lower Case
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

# @param {String} s
# @return {String}
def greatest_letter(s)
  lower = Array.new(26, false)
  upper = Array.new(26, false)
  s.each_char do |c|
    if c >= "a" && c <= "z"
      lower[c.ord - 97] = true
    else
      upper[c.ord - 65] = true
    end
  end
  25.downto(0) do |i|
    return (65 + i).chr if lower[i] && upper[i]
  end
  ""
end
