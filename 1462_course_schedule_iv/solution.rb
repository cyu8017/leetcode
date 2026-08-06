# LeetCode 1462 - Course Schedule Iv
# https://leetcode.com/problems/course-schedule-iv/

def check_if_prerequisite(num_courses, prerequisites, queries)
  reach = Array.new(num_courses) { Array.new(num_courses, false) }
  prerequisites.each { |a, b| reach[a][b] = true }
  num_courses.times do |k|
    num_courses.times do |i|
      next unless reach[i][k]
      num_courses.times { |j| reach[i][j] ||= reach[k][j] }
    end
  end
  queries.map { |a, b| reach[a][b] }
end
