# LeetCode 0354 - Russian Doll Envelopes
# https://leetcode.com/problems/russian-doll-envelopes/

class Solution
  def max_envelopes(envelopes)
    sorted = envelopes.sort_by { |width, height| [width, -height] }
    tails = []

    sorted.each do |_, height|
      index = bisect_left(tails, height)
      if index == tails.length
        tails << height
      else
        tails[index] = height
      end
    end

    tails.length
  end

  alias_method :maxEnvelopes, :max_envelopes

  private

  def bisect_left(array, target)
    left = 0
    right = array.length
    while left < right
      mid = (left + right) / 2
      if array[mid] < target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end
end
