# LeetCode 0277 - Find the Celebrity
# https://leetcode.com/problems/find-the-celebrity/

class Solution
  def findCelebrity(graph)
    n = graph.length
    candidate = 0
    (1...n).each do |person|
      candidate = person if graph[candidate][person] == 1
    end
    (0...n).each do |person|
      next if person == candidate
      return -1 if graph[candidate][person] == 1 || graph[person][candidate] == 0
    end
    candidate
  end
end
