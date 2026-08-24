// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution {
    func minMovesToSeat(_ seats: [Int], _ students: [Int]) -> Int {
        let seats = seats.sorted()
        let students = students.sorted()
        return zip(seats, students).reduce(0) { $0 + abs($1.0 - $1.1) }
    }
}
