# LeetCode 1560 - Most Visited Sector in  a Circular Track
# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

# @param {Integer} n
# @param {Integer[]} rounds
# @return {Integer[]}
def most_visited(n, rounds)
  start = rounds[0]
  ending = rounds[-1]
  if start <= ending
    (start..ending).to_a
  else
    (1..ending).to_a + (start..n).to_a
  end
end
