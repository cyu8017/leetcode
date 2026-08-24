// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

impl Solution {
    pub fn minimum_cost(s: String, t: String, flip_cost: i32, swap_cost: i32, cross_cost: i32) -> i64 {
        let mut diff = [0i64; 2];
        let sb = s.as_bytes();
        let tb = t.as_bytes();
        for i in 0..sb.len() {
            if sb[i] != tb[i] {
                diff[(sb[i] - b'0') as usize] += 1;
            }
        }
        let mut ans = (diff[0] + diff[1]) * flip_cost as i64;
        let mx = diff[0].max(diff[1]);
        let mn = diff[0].min(diff[1]);
        ans = ans.min(mn * swap_cost as i64 + (mx - mn) * flip_cost as i64);
        let avg = (mx + mn) / 2;
        ans = ans.min(
            (avg - mn) * cross_cost as i64 + avg * swap_cost as i64 + (mx + mn - avg * 2) * flip_cost as i64,
        );
        ans
    }
}
