# LeetCode 0170 - Two Sum III - Data structure design
# https://leetcode.com/problems/two-sum-iii-data-structure-design/

class TwoSum
  def initialize
    @counts = Hash.new(0)
  end

  def add(number)
    @counts[number] += 1
  end

  def find(value)
    @counts.each do |number, count|
      complement = value - number
      return true if complement == number && count >= 2
      return true if complement != number && @counts.key?(complement)
    end
    false
  end
end