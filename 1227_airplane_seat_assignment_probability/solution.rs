// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

impl Solution {
    pub fn nth_person_gets_nth_seat(n: i32) -> f64 {
        if n == 1 {
            1.0
        } else {
            0.5
        }
    }
}
