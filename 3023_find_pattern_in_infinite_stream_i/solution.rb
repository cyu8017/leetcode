# LeetCode 3023 - Find Pattern in Infinite Stream I
# https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

class InfiniteStream
  def initialize(bits)
    @bits = bits.reject { |x| x == "..." }
    @i = 0
  end

  def next
    v = @bits[@i]
    @i += 1
    v
  end
end

# @param {Object} stream
# @param {Integer[]} pattern
# @return {Integer}
def find_pattern(stream, pattern)
  stream = InfiniteStream.new(stream) if stream.is_a?(Array)
  a = 0
  b = 0
  m = pattern.length
  half = m >> 1
  mask1 = (1 << half) - 1
  mask2 = (1 << (m - half)) - 1
  half.times { |i| a |= pattern[i] << (half - 1 - i) }
  (half...m).each { |i| b |= pattern[i] << (m - 1 - i) }
  x = 0
  y = 0
  i = 1
  loop do
    v = stream.next
    y = y << 1 | v
    v = (y >> (m - half)) & 1
    y &= mask2
    x = x << 1 | v
    x &= mask1
    return i - m if i >= m && a == x && b == y

    i += 1
  end
end

def solve(*args)
  find_pattern(*args)
end
