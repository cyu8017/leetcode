# LeetCode 0900 - RLE Iterator
# https://leetcode.com/problems/rle-iterator/

class RLEIterator
  def initialize(encoding)
    @enc = encoding
    @i = 0
  end

  def next(n)
    while @i < @enc.length
      if @enc[@i] >= n
        @enc[@i] -= n
        return @enc[@i + 1]
      end
      n -= @enc[@i]
      @i += 2
    end
    -1
  end
end
