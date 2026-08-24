# LeetCode 3477 - Fruits Into Baskets II
# https://leetcode.com/problems/fruits-into-baskets-ii/

# @param {Integer[]} fruits
# @param {Integer[]} baskets
# @return {Integer}
def num_of_unplaced_fruits(fruits, baskets)
  used = Array.new(baskets.length, false)
  unplaced = 0
  fruits.each do |f|
    placed = false
    (0...baskets.length).each do |j|
      next unless !used[j] && baskets[j] >= f

      used[j] = true
      placed = true
      break
    end
    unplaced += 1 unless placed
  end
  unplaced
end
