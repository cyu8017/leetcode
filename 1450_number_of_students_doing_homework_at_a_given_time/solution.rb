# LeetCode 1450 - Number Of Students Doing Homework At A Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

def busy_student(start_time, end_time, query_time)
  start_time.zip(end_time).count { |start, ending| start <= query_time && query_time <= ending }
end
