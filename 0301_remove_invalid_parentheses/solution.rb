# LeetCode 0301 - Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/

class Solution
  def removeInvalidParentheses(s)
    valid = lambda do |text|
      balance = 0
      text.each_char do |char|
        if char == "("
          balance += 1
        elsif char == ")"
          return false if balance.zero?

          balance -= 1
        end
      end
      balance.zero?
    end

    result = {}
    queue = [s]
    visited = { s => true }
    found = false
    until queue.empty?
      level_size = queue.length
      level_size.times do
        current = queue.shift
        if valid.call(current)
          result[current] = true
          found = true
        end
        next if found

        current.length.times do |index|
          next unless "()".include?(current[index])

          nxt = current[0...index] + current[(index + 1)..]
          next if visited[nxt]

          visited[nxt] = true
          queue << nxt
        end
      end
    end
    result.keys
  end
end
