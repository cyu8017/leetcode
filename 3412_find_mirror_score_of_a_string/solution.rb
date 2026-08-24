# LeetCode 3412 - Find Mirror Score of a String
# https://leetcode.com/problems/find-mirror-score-of-a-string/

# @param {String} s
# @return {Integer}
def calculate_score(s)
  stacks = Array.new(26) { [] }
  ans = 0
  s.each_char.with_index do |ch, i|
    ci = ch.ord - 97
    mir = 25 - ci
    if !stacks[mir].empty?
      j = stacks[mir].pop
      ans += i - j
    else
      stacks[ci] << i
    end
  end
  ans
end
