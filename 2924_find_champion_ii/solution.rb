# LeetCode 2924 - Find Champion II
# https://leetcode.com/problems/find-champion-ii/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_champion(n, edges)
  indeg = Array.new(n, 0)
  edges.each { |e| indeg[e[1]] += 1 }
  ans = -1
  (0...n).each do |i|
    next unless indeg[i] == 0
    return -1 if ans != -1

    ans = i
  end
  ans
end
