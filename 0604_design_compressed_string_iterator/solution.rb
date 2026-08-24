# LeetCode 0604 - Design Compressed String Iterator
# https://leetcode.com/problems/design-compressed-string-iterator/

class StringIterator
  def initialize(compressed_string)
    @chars = []
    @counts = []
    i = 0
    n = compressed_string.length
    while i < n
      ch = compressed_string[i]
      i += 1
      j = i
      j += 1 while j < n && compressed_string[j] =~ /\d/
      @chars << ch
      @counts << compressed_string[i...j].to_i
      i = j
    end
    @index = 0
  end

  def next
    return " " unless has_next

    ch = @chars[@index]
    @counts[@index] -= 1
    @index += 1 if @counts[@index].zero?
    ch
  end

  def has_next
    @index < @chars.length
  end
end
