# LeetCode 1405 - Longest Happy String
# https://leetcode.com/problems/longest-happy-string/

def longest_diverse_string(a, b, c)
  heap = []
  [[a, 'a'], [b, 'b'], [c, 'c']].each { |count, char| heap << [-count, char] if count > 0 }
  heap.sort!
  answer = []
  until heap.empty?
    count, char = heap.shift
    if answer.length >= 2 && answer[-1] == answer[-2] && answer[-1] == char
      break if heap.empty?
      count2, char2 = heap.shift
      answer << char2
      heap << [count2 + 1, char2] if count2 + 1 < 0
      heap << [count, char]
      heap.sort!
    else
      answer << char
      heap << [count + 1, char] if count + 1 < 0
      heap.sort!
    end
  end
  answer.join
end
