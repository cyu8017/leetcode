// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

impl Solution {
    pub fn good_days_to_rob_bank(security: Vec<i32>, time: i32) -> Vec<i32> {
        let n = security.len();
        let time = time as usize;
        if time == 0 {
            return (0..n as i32).collect();
        }
        let mut left = vec![0; n];
        let mut right = vec![0; n];
        for i in 1..n {
            if security[i] <= security[i - 1] {
                left[i] = left[i - 1] + 1;
            }
        }
        for i in (0..n - 1).rev() {
            if security[i] <= security[i + 1] {
                right[i] = right[i + 1] + 1;
            }
        }
        (time..n - time)
            .filter(|&i| left[i] >= time && right[i] >= time)
            .map(|i| i as i32)
            .collect()
    }
}
