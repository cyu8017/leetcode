# LeetCode 0171 - Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution
  def title_to_number(column_title)
    column_title.each_byte.reduce(0) do |result, byte|
      result * 26 + byte - "A".ord + 1
    end
  end
end