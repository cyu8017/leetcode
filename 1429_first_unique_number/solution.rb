# LeetCode 1429 - First Unique Number
# https://leetcode.com/problems/first-unique-number/

class FirstUnique
  def initialize(nums)
    @counts = Hash.new(0)
    @unique = {}
    nums.each { |value| add(value) }
  end

  def show_first_unique
    @unique.each_key { |k| return k }
    -1
  end

  def add(value)
    @counts[value] += 1
    if @counts[value] == 1
      @unique[value] = true
    else
      @unique.delete(value)
    end
  end
end
