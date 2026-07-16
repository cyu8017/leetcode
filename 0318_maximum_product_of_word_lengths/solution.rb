# LeetCode 0318 - Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution
  def maxProduct(words)
    masks = []
    lengths = []
    words.each do |word|
      mask = 0
      valid = true
      word.each_char do |char|
        bit = 1 << (char.ord - 'a'.ord)
        if (mask & bit) != 0
          valid = false
          break
        end
        mask |= bit
      end
      masks << (valid ? mask : 0)
      lengths << word.length
    end

    best = 0
    (0...words.length).each do |left|
      next if masks[left] == 0

      ((left + 1)...words.length).each do |right|
        next if masks[right] == 0
        next unless (masks[left] & masks[right]).zero?

        best = [best, lengths[left] * lengths[right]].max
      end
    end
    best
  end
end
