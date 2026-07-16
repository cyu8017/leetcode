# LeetCode 0306 - Additive Number
# https://leetcode.com/problems/additive-number/

class Solution
  def isAdditiveNumber(num)
    valid = lambda do |first, second, start|
      return false if (first.length > 1 && first[0] == "0") || (second.length > 1 && second[0] == "0")

      while start < num.length
        total = (first.to_i + second.to_i).to_s
        return false unless num.start_with?(total, start)

        first = second
        second = total
        start += total.length
      end
      true
    end

    (1...num.length).each do |first_end|
      ((first_end + 1)...num.length).each do |second_end|
        return true if valid.call(num[0...first_end], num[first_end...second_end], second_end)
      end
    end
    false
  end
end
