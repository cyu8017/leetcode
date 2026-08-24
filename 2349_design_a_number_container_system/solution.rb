# LeetCode 2349 - Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers
  def initialize
    @idx = {}
    @heap = {}
  end

  def change(index, number)
    @idx[index] = number
    @heap[number] ||= []
    @heap[number] << index
    nil
  end

  def find(number)
    h = @heap[number]
    return -1 if h.nil? || h.empty?
    h.sort!
    until h.empty?
      i = h[0]
      return i if @idx[i] == number
      h.shift
    end
    -1
  end
end
