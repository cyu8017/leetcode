# LeetCode 3484 - Design Spreadsheet
# https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet
  def initialize(_rows)
    @cells = {}
  end

  def set_cell(cell, value)
    @cells[cell] = value
  end

  def reset_cell(cell)
    @cells.delete(cell)
  end

  def get_value(formula)
    formula = formula[1..] if formula && formula[0] == "="
    total = 0
    start = 0
    while start < formula.length
      plus = formula.index("+", start)
      p = plus.nil? ? formula[start..] : formula[start...plus]
      is_num = !p.empty? && ((p[0] >= "0" && p[0] <= "9") || (p[0] == "-" && p.length > 1))
      if is_num
        (1...p.length).each do |i|
          if p[i] < "0" || p[i] > "9"
            is_num = false
            break
          end
        end
      end
      total += is_num ? p.to_i : (@cells[p] || 0)
      break if plus.nil?

      start = plus + 1
    end
    total
  end
end
