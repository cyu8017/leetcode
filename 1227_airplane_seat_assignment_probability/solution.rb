# LeetCode 1227 - Airplane Seat Assignment Probability
# https://leetcode.com/problems/airplane-seat-assignment-probability/

# @param {Integer} n
# @return {Float}
def nth_person_gets_nth_seat(n)
  n == 1 ? 1.0 : 0.5
end
