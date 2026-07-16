# LeetCode 0421 - Maximum XOR of Two Numbers in an Array
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution
  def find_maximum_xor(nums)
    maximum = nums.max
    max_bit = maximum.bit_length
    root = {}
    best = 0

    nums.each do |number|
      node = root
      (max_bit - 1).downto(0) do |bit|
        current = (number >> bit) & 1
        node[current] ||= {}
        node = node[current]
      end
    end

    nums.each do |number|
      node = root
      candidate = 0
      (max_bit - 1).downto(0) do |bit|
        current = (number >> bit) & 1
        target = 1 - current
        if node.key?(target)
          candidate |= 1 << bit
          node = node[target]
        else
          node = node[current]
        end
      end
      best = [best, candidate].max
    end

    best
  end

  alias_method :findMaximumXOR, :find_maximum_xor
end
