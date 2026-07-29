# LeetCode 1049 - Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/

# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight_ii(stones)
  total = stones.sum
  reachable = { 0 => true }
  stones.each do |stone|
    nxt = reachable.dup
    reachable.each_key { |s| nxt[s + stone] = true }
    reachable = nxt
  end
  reachable.keys.map { |s| (total - 2 * s).abs }.min
end
