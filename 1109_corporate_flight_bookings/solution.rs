// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

impl Solution {
    pub fn corp_flight_bookings(bookings: Vec<Vec<i32>>, n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut diff = vec![0; n + 1];
        for b in bookings {
            diff[(b[0] - 1) as usize] += b[2];
            diff[b[1] as usize] -= b[2];
        }
        let mut ans = vec![0; n];
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            ans[i] = cur;
        }
        ans
    }
}
