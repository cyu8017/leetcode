// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

impl Solution {
    pub fn count_days_together(
        arrive_alice: String,
        leave_alice: String,
        arrive_bob: String,
        leave_bob: String,
    ) -> i32 {
        const DAYS: [i32; 12] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        let to_day = |s: &str| {
            let b = s.as_bytes();
            let m = (b[0] - b'0') as i32 * 10 + (b[1] - b'0') as i32;
            let d = (b[3] - b'0') as i32 * 10 + (b[4] - b'0') as i32;
            let mut res = d;
            for i in 0..(m - 1) as usize {
                res += DAYS[i];
            }
            res
        };
        let a1 = to_day(&arrive_alice);
        let a2 = to_day(&leave_alice);
        let b1 = to_day(&arrive_bob);
        let b2 = to_day(&leave_bob);
        let start = a1.max(b1);
        let end = a2.min(b2);
        if end < start {
            0
        } else {
            end - start + 1
        }
    }
}
