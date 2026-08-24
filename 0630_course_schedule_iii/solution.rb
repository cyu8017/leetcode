# LeetCode 0630 - Course Schedule III
# https://leetcode.com/problems/course-schedule-iii/

# @param {Integer[][]} courses
# @return {Integer}
def schedule_course(courses)
  courses = courses.sort_by { |course| course[1] }
  heap = []
  time = 0

  courses.each do |duration, last_day|
    if time + duration <= last_day
      heap << duration
      time += duration
    elsif !heap.empty? && heap.max > duration
      max_duration = heap.max
      heap.delete_at(heap.index(max_duration))
      time += duration - max_duration
      heap << duration
    end
  end

  heap.length
end
