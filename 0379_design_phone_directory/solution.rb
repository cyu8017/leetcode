# LeetCode 0379 - Design Phone Directory
# https://leetcode.com/problems/design-phone-directory/

require "set"

class PhoneDirectory
  def initialize(max_numbers)
    @available = Set.new(0...max_numbers)
  end

  def get
    return -1 if @available.empty?

    number = @available.min
    @available.delete(number)
    number
  end

  def check(number)
    @available.include?(number)
  end

  def release(number)
    @available.add(number)
  end
end
