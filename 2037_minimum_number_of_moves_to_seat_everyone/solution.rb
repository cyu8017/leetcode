# LeetCode 2037 - Minimum Number of Moves to Seat Everyone
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

# @param {Integer[]} seats
# @param {Integer[]} students
# @return {Integer}
def min_moves_to_seat(seats, students)
  seats.sort!
  students.sort!
  seats.zip(students).sum { |a, b| (a - b).abs }
end
