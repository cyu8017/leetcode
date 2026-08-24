# LeetCode 3227 - Vowels Game in a String
# https://leetcode.com/problems/vowels-game-in-a-string/

# @param {String} s
# @return {Boolean}
def does_alice_win(s)
  s.each_char { |c| return true if "aeiou".include?(c) }
  false
end
