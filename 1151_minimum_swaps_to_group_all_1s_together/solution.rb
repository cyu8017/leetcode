# LeetCode 1151 - Minimum Swaps to Group All 1's Together
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

# @param {Integer[]} data
# @return {Integer}
def min_swaps(data)
  ones = data.sum
  return 0 if ones <= 1
  cur = data[0...ones].sum
  best = cur
  (ones...data.length).each do |i|
    cur += data[i] - data[i - ones]
    best = [best, cur].max
  end
  ones - best
end
