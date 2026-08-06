# LeetCode 1700 - Number of Students Unable to Eat Lunch
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

# @param {Integer[]} students
# @param {Integer[]} sandwiches
# @return {Integer}
def count_students(students, sandwiches)
  c = Hash.new(0)
  students.each { |x| c[x] += 1 }
  sandwiches.each_with_index do |x, i|
    return students.length - i if c[x].zero?
    c[x] -= 1
  end
  0
end
