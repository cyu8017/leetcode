# LeetCode 0269 - Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/

require 'set'

# @param {String[]} words
# @return {String}
def alien_order(words)
  graph = Hash.new { |hash, key| hash[key] = Set.new }
  indegree = Hash.new(0)

  words.each do |word|
    word.each_char do |char|
      graph[char]
      indegree[char] = 0 unless indegree.key?(char)
    end
  end

  words.each_cons(2) do |first, second|
    if first.length > second.length && first.start_with?(second)
      return ''
    end
    limit = [first.length, second.length].min
    (0...limit).each do |index|
      left = first[index]
      right = second[index]
      next if left == right

      unless graph[left].include?(right)
        graph[left].add(right)
        indegree[right] += 1
      end
      break
    end
  end

  queue = indegree.select { |_, degree| degree.zero? }.keys
  order = +''
  until queue.empty?
    char = queue.shift
    order << char
    graph[char].each do |next_char|
      indegree[next_char] -= 1
      queue << next_char if indegree[next_char].zero?
    end
  end

  order.length == indegree.length ? order : ''
end
