# LeetCode 1927 - Sum Game
# https://leetcode.com/problems/sum-game/

# @param {String} num
# @return {Boolean}
def sum_game(num)
  half = num.length / 2
  score = lambda do |s|
    q = 0
    dig = 0
    s.each_char do |c|
      if c == "?"
        q += 1
      else
        dig += c.ord - 48
      end
    end
    dig * 2 + q * 9
  end
  score.call(num[0...half]) != score.call(num[half..])
end
