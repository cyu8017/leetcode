# LeetCode 0393 - UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/

class Solution
  def valid_utf8(data)
    remaining = 0

    data.each do |byte|
      byte &= 0xFF
      if remaining == 0
        if byte >> 7 == 0b0
          next
        elsif byte >> 5 == 0b110
          remaining = 1
        elsif byte >> 4 == 0b1110
          remaining = 2
        elsif byte >> 3 == 0b11110
          remaining = 3
        else
          return false
        end
      elsif byte >> 6 != 0b10
        return false
      else
        remaining -= 1
      end
    end

    remaining == 0
  end

  alias_method :validUtf8, :valid_utf8
end
