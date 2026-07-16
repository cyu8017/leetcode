# LeetCode 0210 - Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Integer[]}
def find_order(num_courses, prerequisites)
  graph = Array.new(num_courses) { [] }
  indegree = Array.new(num_courses, 0)
  prerequisites.each do |course, prerequisite|
    graph[prerequisite] << course
    indegree[course] += 1
  end

  order = (0...num_courses).select { |course| indegree[course].zero? }
  index = 0
  while index < order.length
    course = order[index]
    index += 1
    graph[course].each do |next_course|
      indegree[next_course] -= 1
      order << next_course if indegree[next_course].zero?
    end
  end
  order.length == num_courses ? order : []
end