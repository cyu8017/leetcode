# LeetCode 0207 - Course Schedule
# https://leetcode.com/problems/course-schedule/

# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
  graph = Array.new(num_courses) { [] }
  indegree = Array.new(num_courses, 0)
  prerequisites.each do |course, prerequisite|
    graph[prerequisite] << course
    indegree[course] += 1
  end

  queue = (0...num_courses).select { |course| indegree[course].zero? }
  index = 0
  while index < queue.length
    course = queue[index]
    index += 1
    graph[course].each do |next_course|
      indegree[next_course] -= 1
      queue << next_course if indegree[next_course].zero?
    end
  end
  queue.length == num_courses
end