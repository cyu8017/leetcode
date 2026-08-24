# LeetCode 0799 - Champagne Tower
# https://leetcode.com/problems/champagne-tower/

# @param {Integer} poured
# @param {Integer} query_row
# @param {Integer} query_glass
# @return {Float}
def champagne_tower(poured, query_row, query_glass)
  row = [poured.to_f]
  query_row.times do |r|
    next_row = Array.new(r + 2, 0.0)
    row.each_with_index do |amount, i|
      overflow = (amount - 1.0) / 2.0
      if overflow > 0
        next_row[i] += overflow
        next_row[i + 1] += overflow
      end
    end
    row = next_row
  end
  [1.0, row[query_glass]].min
end
