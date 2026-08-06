// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

use std::collections::HashMap;

impl Solution {
    pub fn max_number_of_families(n: i32, reserved_seats: Vec<Vec<i32>>) -> i32 {
        let mut rows: HashMap<i32, i32> = HashMap::new();
        for seat in reserved_seats {
            let (r, c) = (seat[0], seat[1]);
            if (2..=9).contains(&c) {
                *rows.entry(r).or_insert(0) |= 1 << (c - 2);
            }
        }
        let mut ans = 2 * (n - rows.len() as i32);
        for &m in rows.values() {
            let left = m & 0b0000_1111 == 0;
            let right = m & 0b1111_0000 == 0;
            let middle = m & 0b0011_1100 == 0;
            ans += if left && right {
                2
            } else {
                i32::from(left || right || middle)
            };
        }
        ans
    }
}
