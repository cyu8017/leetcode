# LeetCode 1165 - Single-Row Keyboard
# https://leetcode.com/problems/single-row-keyboard/

# @param {String} keyboard
# @param {String} word
# @return {Integer}
def calculate_time(keyboard, word)
  pos = {}
  keyboard.each_char.with_index { |ch, i| pos[ch] = i }
  ans = 0
  prev = 0
  word.each_char do |ch|
    ans += (pos[ch] - prev).abs
    prev = pos[ch]
  end
  ans
end
