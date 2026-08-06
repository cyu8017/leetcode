# LeetCode 1533 - Find the Index of the Large Integer
# https://leetcode.com/problems/find-the-index-of-the-large-integer/

class ArrayReader
  def initialize(arr)
    @arr = arr
  end

  def compare_sub(l, r, x, y)
    a = @arr[l..r].sum
    b = @arr[x..y].sum
    a <=> b
  end

  def length
    @arr.length
  end
end

# @param {ArrayReader|Integer[]} reader
# @return {Integer}
def get_index(reader)
  reader = ArrayReader.new(reader) if reader.is_a?(Array)
  left = 0
  right = reader.length - 1
  while left < right
    length = right - left + 1
    half = length / 2
    result = reader.compare_sub(left, left + half - 1, right - half + 1, right)
    if result == 0
      return left + half
    elsif result > 0
      right = left + half - 1
    else
      left = right - half + 1
    end
  end
  left
end
