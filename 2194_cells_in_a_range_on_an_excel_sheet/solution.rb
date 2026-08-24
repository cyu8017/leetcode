# LeetCode 2194 - Cells in a Range on an Excel Sheet
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

# @param {String} s
# @return {String[]}
def cells_in_range(s)
  ans = []
  (s[0].ord..s[3].ord).each do |c|
    (s[1].ord..s[4].ord).each { |r| ans << c.chr + r.chr }
  end
  ans
end
