# LeetCode 2300 - Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

# @param {Integer[]} spells
# @param {Integer[]} potions
# @param {Integer} success
# @return {Integer[]}
def successful_pairs(spells, potions, success)
  potions = potions.sort
  m = potions.length
  spells.map do |spell|
    lo = 0
    hi = m
    while lo < hi
      mid = (lo + hi) >> 1
      if spell * potions[mid] >= success
        hi = mid
      else
        lo = mid + 1
      end
    end
    m - lo
  end
end
