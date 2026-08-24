// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

impl Solution {
    pub fn min_moves_to_seat(mut seats: Vec<i32>, mut students: Vec<i32>) -> i32 {
        seats.sort_unstable();
        students.sort_unstable();
        seats.iter().zip(students.iter()).map(|(a, b)| (a - b).abs()).sum()
    }
}
