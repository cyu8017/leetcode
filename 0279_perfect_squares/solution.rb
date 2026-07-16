# LeetCode 0279 - Perfect Squares
# https://leetcode.com/problems/perfect-squares/

class Solution
  def numSquares(n)
    squares = []
    value = 1
    while value * value <= n
      squares << value * value
      value += 1
    end

    queue = [[n, 0]]
    visited = { n => true }

    until queue.empty?
      remain, steps = queue.shift
      return steps if remain == 0

      squares.each do |square|
        nxt = remain - square
        break if nxt.negative?

        unless visited[nxt]
          visited[nxt] = true
          queue << [nxt, steps + 1]
        end
      end
    end
    0
  end
end
