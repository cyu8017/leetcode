# LeetCode 1825 - Finding MK Average
# https://leetcode.com/problems/finding-mk-average/

class MKAverage
  # @param {Integer} m
  # @param {Integer} k
  def initialize(m, k)
    @m = m
    @k = k
    @stream = []
  end

  # @param {Integer} num
  # @return {Void}
  def addElement(num)
    @stream << num
    nil
  end

  # @return {Integer}
  def calculateMKAverage
    return -1 if @stream.length < @m
    window = @stream[-@m..].sort
    middle = window[@k...(@m - @k)]
    middle.sum / middle.length
  end
end
