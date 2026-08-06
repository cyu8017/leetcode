# LeetCode 1181 - Before and After Puzzle
# https://leetcode.com/problems/before-and-after-puzzle/

# @param {String[]} phrases
# @return {String[]}
def before_and_after_puzzles(phrases)
  split = phrases.map(&:split)
  result = {}
  split.each_with_index do |a, i|
    split.each_with_index do |b, j|
      next if i == j
      result[(a + b[1..]).join(" ")] = true if a[-1] == b[0]
    end
  end
  result.keys.sort
end
