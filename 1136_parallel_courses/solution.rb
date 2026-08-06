# LeetCode 1136 - Parallel Courses
# https://leetcode.com/problems/parallel-courses/

# @param {Integer} n
# @param {Integer[][]} relations
# @return {Integer}
def minimum_semesters(n, relations)
  graph = Array.new(n + 1) { [] }
  indegree = Array.new(n + 1, 0)
  relations.each do |prev, nxt|
    graph[prev] << nxt
    indegree[nxt] += 1
  end
  queue = (1..n).select { |i| indegree[i] == 0 }
  semesters = 0
  taken = 0
  until queue.empty?
    semesters += 1
    queue.length.times do
      course = queue.shift
      taken += 1
      graph[course].each do |nxt|
        indegree[nxt] -= 1
        queue << nxt if indegree[nxt] == 0
      end
    end
  end
  taken == n ? semesters : -1
end
