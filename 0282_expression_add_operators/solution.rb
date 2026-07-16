# LeetCode 0282 - Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/

class Solution
  def addOperators(num, target)
    result = []

    backtrack = lambda do |index, path, value, previous|
      if index == num.length
        result << path if value == target
        return
      end
      (index...num.length).each do |end_index|
        break if end_index > index && num[index] == "0"

        current_str = num[index..end_index]
        current = current_str.to_i
        if index == 0
          backtrack.call(end_index + 1, current_str, current, current)
        else
          backtrack.call(end_index + 1, path + "+" + current_str, value + current, current)
          backtrack.call(end_index + 1, path + "-" + current_str, value - current, -current)
          backtrack.call(
            end_index + 1,
            path + "*" + current_str,
            value - previous + previous * current,
            previous * current
          )
        end
      end
    end

    backtrack.call(0, "", 0, 0)
    result
  end
end
