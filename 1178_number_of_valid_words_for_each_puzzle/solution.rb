# LeetCode 1178 - Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

# @param {String[]} words
# @param {String[]} puzzles
# @return {Integer[]}
def find_num_of_valid_words(words, puzzles)
  mask_of = lambda do |str|
    mask = 0
    str.each_char { |ch| mask |= 1 << (ch.ord - 97) }
    mask
  end
  freq = Hash.new(0)
  words.each { |w| freq[mask_of.call(w)] += 1 }
  puzzles.map do |puzzle|
    first = 1 << (puzzle[0].ord - 97)
    full = mask_of.call(puzzle)
    sub = full
    total = 0
    loop do
      total += freq[sub] if (sub & first) != 0
      break if sub == 0
      sub = (sub - 1) & full
    end
    total
  end
end
