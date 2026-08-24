# LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

# @param {String} s
# @return {Boolean}
def are_numbers_ascending(s)
  prev = -1
  s.split(" ").each do |tok|
    next if tok.empty?
    next unless tok[0] >= "0" && tok[0] <= "9"

    v = tok.to_i
    return false if v <= prev

    prev = v
  end
  true
end
