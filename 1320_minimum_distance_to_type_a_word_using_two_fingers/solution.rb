# LeetCode 1320 - Minimum Distance To Type A Word Using Two Fingers
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

def minimum_distance(word)
  distance = lambda do |a, b|
    return 0 if a == 26
    (a / 6 - b / 6).abs + (a % 6 - b % 6).abs
  end
  letters = word.chars.map { |ch| ch.ord - 65 }
  dp = { 26 => 0 }
  previous = letters[0]
  letters[1..].each do |current|
    nxt = {}
    dp.each do |free, cost|
      nxt[free] = [nxt.fetch(free, 10**9), cost + distance.call(previous, current)].min
      nxt[previous] = [nxt.fetch(previous, 10**9), cost + distance.call(free, current)].min
    end
    dp = nxt
    previous = current
  end
  dp.values.min
end
