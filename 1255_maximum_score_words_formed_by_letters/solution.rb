# LeetCode 1255 - Maximum Score Words Formed by Letters
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

# @param {String[]} words
# @param {Character[]} letters
# @param {Integer[]} score
# @return {Integer}
def max_score_words(words, letters, score)
  available = Hash.new(0)
  letters.each { |ch| available[ch] += 1 }
  counts = words.map do |word|
    c = Hash.new(0)
    word.each_char { |ch| c[ch] += 1 }
    c
  end
  values = words.map { |word| word.chars.sum { |ch| score[ch.ord - 97] } }
  dfs = nil
  dfs = lambda do |i|
    return 0 if i == words.length
    best = dfs.call(i + 1)
    if counts[i].all? { |ch, v| v <= available[ch] }
      counts[i].each { |ch, v| available[ch] -= v }
      best = [best, values[i] + dfs.call(i + 1)].max
      counts[i].each { |ch, v| available[ch] += v }
    end
    best
  end
  dfs.call(0)
end
