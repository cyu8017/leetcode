# LeetCode 2728 - Count Houses in a Circular Street
# https://leetcode.com/problems/count-houses-in-a-circular-street/

class Street
  def initialize(doors)
    @doors = doors
    @i = 0
  end

  def closeDoor
    @doors[@i] = 0
  end

  def openDoor
    @doors[@i] = 1
  end

  def isDoorOpen
    @doors[@i] == 1
  end

  def moveRight
    @i = (@i + 1) % @doors.length
  end
end

# @param {Object} street
# @param {Integer} k
# @return {Integer}
def house_count(street, k)
  street = Street.new(street) if street.is_a?(Array)
  k.times do
    street.closeDoor
    street.moveRight
  end
  ans = 0
  loop do
    ans += 1
    street.openDoor
    street.moveRight
    break if street.isDoorOpen
  end
  ans
end
