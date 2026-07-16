# LeetCode 0127 - Word Ladder
# https://leetcode.com/problems/word-ladder/

# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {Integer}
def ladder_length(begin_word, end_word, word_list)
  words = word_list.to_h { |word| [word, true] }
  return 0 unless words.key?(end_word)

  queue = [[begin_word, 1]]
  visited = { begin_word => true }
  until queue.empty?
    word, steps = queue.shift
    return steps if word == end_word

    characters = word.chars
    characters.each_index do |index|
      original = characters[index]
      ("a".."z").each do |letter|
        characters[index] = letter
        candidate = characters.join
        next unless words.key?(candidate) && !visited.key?(candidate)

        visited[candidate] = true
        queue << [candidate, steps + 1]
      end
      characters[index] = original
    end
  end
  0
end