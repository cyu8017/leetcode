# LeetCode 1656 - Design an Ordered Stream
# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream
  # @param {Integer} n
  def initialize(n)
    @a = Array.new(n + 1)
    @p = 1
  end

  # @param {Integer} id_key
  # @param {String} value
  # @return {String[]}
  def insert(id_key, value)
    @a[id_key] = value
    out = []
    while @p < @a.length && !@a[@p].nil?
      out << @a[@p]
      @p += 1
    end
    out
  end
end
