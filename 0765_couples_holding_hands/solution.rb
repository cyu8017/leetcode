# LeetCode 0765 - Couples Holding Hands
# https://leetcode.com/problems/couples-holding-hands/

# @param {Integer[]} row
# @return {Integer}
def min_swaps_couples(row)
  pos = {}
  row.each_with_index { |person, index| pos[person] = index }
  swaps = 0
  (0...row.length).step(2) do |i|
    partner = row[i] ^ 1
    next if row[i + 1] == partner

    j = pos[partner]
    pos[row[i + 1]] = j
    row[j] = row[i + 1]
    row[i + 1] = partner
    pos[partner] = i + 1
    swaps += 1
  end
  swaps
end
