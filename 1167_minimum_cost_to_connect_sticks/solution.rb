# LeetCode 1167 - Minimum Cost to Connect Sticks
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/

# @param {Integer[]} sticks
# @return {Integer}
def connect_sticks(sticks)
  return 0 if sticks.length <= 1
  heap = sticks.sort
  ans = 0
  while heap.length > 1
    cost = heap.shift + heap.shift
    ans += cost
    idx = heap.bsearch_index { |x| x >= cost } || heap.length
    heap.insert(idx, cost)
  end
  ans
end
