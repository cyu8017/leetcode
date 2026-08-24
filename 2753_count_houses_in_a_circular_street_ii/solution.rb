# LeetCode 2753 - Count Houses in a Circular Street II
# https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

class Street
  def initialize(doors)
    @doors = doors
    @i = 0
  end

  def closeDoor
    @doors[@i] = 0
  end

  def isDoorOpen
    @doors[@i] == 1
  end

  def moveRight
    @i = (@i + 1) % @doors.length
  end

  def moveLeft
    @i = (@i - 1) % @doors.length
  end
end

# @param {Object} street
# @param {Integer} k
# @return {Integer}
def house_count(street, k)
  street = Street.new(street) if street.is_a?(Array)
  street.moveRight until street.isDoorOpen
  ans = 0
  (1..k).each do |i|
    street.moveRight
    if street.isDoorOpen
      street.closeDoor
      ans = i
    end
  end
  ans
end
