# LeetCode 0551 - Student Attendance Record I
# https://leetcode.com/problems/student-attendance-record-i/

# @param {String} s
# @return {Boolean}
def check_record(s)
  s.count("A") < 2 && !s.include?("LLL")
end
