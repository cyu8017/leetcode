# LeetCode 2351 - First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/

# @param {String} s
# @return {String}
def repeated_character(s)
  seen = Array.new(26, false)
  s.each_char do |c|
    i = c.ord - 97
    return c if seen[i]
    seen[i] = true
  end
  0.chr
end
