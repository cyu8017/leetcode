# LeetCode 0126 - Word Ladder II
# https://leetcode.com/problems/word-ladder-ii/

# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {String[][]}
def find_ladders(begin_word, end_word, word_list)
  words = word_list.to_h { |word| [word, true] }
  return [] unless words.key?(end_word)

  parents = Hash.new { |hash, key| hash[key] = [] }
  visited = { begin_word => true }
  queue = [begin_word]
  found = false

  until queue.empty? || found
    level_visited = {}
    next_queue = []
    queue.each do |word|
      characters = word.chars
      characters.each_index do |index|
        original = characters[index]
        ("a".."z").each do |letter|
          characters[index] = letter
          candidate = characters.join
          next unless words.key?(candidate) && !visited.key?(candidate)

          unless level_visited.key?(candidate)
            level_visited[candidate] = true
            next_queue << candidate
          end
          parents[candidate] << word
          found = true if candidate == end_word
        end
        characters[index] = original
      end
    end
    visited.merge!(level_visited)
    queue = next_queue
  end

  return [] unless found

  results = []
  build = lambda do |word, path|
    if word == begin_word
      results << path.reverse
      next
    end
    parents[word].each { |parent| build.call(parent, path + [parent]) }
  end
  build.call(end_word, [end_word])
  results.sort
end