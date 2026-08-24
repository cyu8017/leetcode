# LeetCode 0954 - Array of Doubled Pairs
# https://leetcode.com/problems/array-of-doubled-pairs/

# @param {Integer[]} arr
# @return {Boolean}
def can_reorder_doubled(arr)
  count = Hash.new(0)
  arr.each { |x| count[x] += 1 }
  count.keys.sort_by(&:abs).each do |x|
    next if count[x] == 0
    return false if count[2 * x] < count[x]

    count[2 * x] -= count[x]
  end
  true
end
