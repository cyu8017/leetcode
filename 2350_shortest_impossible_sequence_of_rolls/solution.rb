# LeetCode 2350 - Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

# @param {Integer[]} rolls
# @param {Integer} k
# @return {Integer}
def shortest_sequence(rolls, k)
  seen = {}
  ans = 1
  rolls.each do |r|
    seen[r] = true
    if seen.length == k
      ans += 1
      seen.clear
    end
  end
  ans
end
