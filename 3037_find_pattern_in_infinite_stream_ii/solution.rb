# LeetCode 3037 - Find Pattern in Infinite Stream II
# https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

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
  lps = get_lps(pattern)
  i = 0
  j = 0
  bit = 0
  read_next = false
  loop do
    unless read_next
      bit = stream.next
      read_next = true
    end
    if bit == pattern[j]
      i += 1
      read_next = false
      j += 1
      return i - j if j == pattern.length
    elsif j > 0
      j = lps[j - 1]
    else
      i += 1
      read_next = false
    end
  end
end

def get_lps(pattern)
  n = pattern.length
  lps = Array.new(n, 0)
  j = 0
  (1...n).each do |i|
    j = lps[j - 1] while j > 0 && pattern[j] != pattern[i]
    if pattern[i] == pattern[j]
      j += 1
      lps[i] = j
    end
  end
  lps
end

def solve(*args)
  find_pattern(*args)
end
