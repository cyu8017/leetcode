# LeetCode 0605 - Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

# @param {Integer[]} flowerbed
# @param {Integer} n
# @return {Boolean}
def can_place_flowers(flowerbed, n)
  return true if n.zero?

  bed = flowerbed.dup
  bed.each_index do |i|
    next if bed[i] == 1

    left_empty = i.zero? || bed[i - 1].zero?
    right_empty = i == bed.length - 1 || bed[i + 1].zero?
    if left_empty && right_empty
      bed[i] = 1
      n -= 1
      return true if n.zero?
    end
  end
  false
end
