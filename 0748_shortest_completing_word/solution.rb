# LeetCode 0748 - Shortest Completing Word
# https://leetcode.com/problems/shortest-completing-word/

# @param {String} license_plate
# @param {String[]} words
# @return {String}
def shortest_completing_word(license_plate, words)
  need = Hash.new(0)
  license_plate.each_char do |ch|
    down = ch.downcase
    need[down] += 1 if down >= "a" && down <= "z"
  end
  best = nil
  words.each do |word|
    counts = Hash.new(0)
    word.each_char { |ch| counts[ch] += 1 }
    next unless need.all? { |ch, cnt| counts[ch] >= cnt }

    best = word if best.nil? || word.length < best.length
  end
  best || ""
end
