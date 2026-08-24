# LeetCode 0631 - Design Excel Sum Formula
# https://leetcode.com/problems/design-excel-sum-formula/

class Excel
  def initialize(height, width)
    @height = height
    @width = width.ord - "A".ord + 1
    @values = Array.new(height + 1) { Array.new(@width, 0) }
    @formulas = {}
  end

  def set(row, column, val)
    col = column.ord - "A".ord
    @formulas.delete([row, col])
    @values[row][col] = val
    nil
  end

  def get(row, column)
    eval_cell(row, column.ord - "A".ord)
  end

  def sum(row, column, numbers)
    col = column.ord - "A".ord
    cells = []
    numbers.each do |token|
      if token.include?(":")
        start_cell, end_cell = token.split(":")
        r1, c1 = parse(start_cell)
        r2, c2 = parse(end_cell)
        (r1..r2).each do |r|
          (c1..c2).each { |c| cells << [r, c] }
        end
      else
        cells << parse(token)
      end
    end
    @formulas[[row, col]] = cells
    eval_cell(row, col)
  end

  private

  def parse(cell)
    [cell[1..].to_i, cell[0].ord - "A".ord]
  end

  def eval_cell(row, col)
    if @formulas.key?([row, col])
      return @formulas[[row, col]].sum { |r, c| eval_cell(r, c) }
    end

    @values[row][col]
  end
end
