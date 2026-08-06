# LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

class Fenwick
  def initialize(n)
    @bit = Array.new(n + 1, 0)
  end

  def add(i, delta)
    i += 1
    while i < @bit.length
      @bit[i] += delta
      i += i & -i
    end
  end

  def sum(i)
    out = 0
    while i > 0
      out += @bit[i]
      i -= i & -i
    end
    out
  end
end

# @param {String} num
# @param {Integer} k
# @return {String}
def min_integer(num, k)
  positions = Array.new(10) { [] }
  num.chars.each_with_index { |ch, i| positions[ch.to_i] << i }
  fw = Fenwick.new(num.length)
  out = []
  num.length.times do
    (0...10).each do |digit|
      next if positions[digit].empty?
      index = positions[digit][0]
      cost = index - fw.sum(index)
      if cost <= k
        k -= cost
        positions[digit].shift
        fw.add(index, 1)
        out << digit.to_s
        break
      end
    end
  end
  out.join
end
