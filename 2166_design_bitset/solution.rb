# LeetCode 2166 - Design Bitset
# https://leetcode.com/problems/design-bitset/

class Bitset
  def initialize(size)
    @size = size
    @bits = Array.new(size, 0)
    @ones = 0
    @flipped = false
  end

  def fix(idx)
    target = @flipped ? 0 : 1
    if @bits[idx] != target
      @bits[idx] = target
      @ones += 1
    end
    nil
  end

  def unfix(idx)
    target = @flipped ? 1 : 0
    if @bits[idx] != target
      @bits[idx] = target
      @ones -= 1
    end
    nil
  end

  def flip
    @flipped = !@flipped
    @ones = @size - @ones
    nil
  end

  def all
    @ones == @size
  end

  def one
    @ones > 0
  end

  def count
    @ones
  end

  def to_string
    b = Array.new(@size)
    @size.times do |i|
      v = @bits[i]
      v ^= 1 if @flipped
      b[i] = v.to_s
    end
    b.join
  end
  alias toString to_string
end
