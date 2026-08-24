struct Solution;
// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

impl Solution {
    pub fn shift_distance(s: String, t: String, next_cost: Vec<i32>, previous_cost: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let sb = s.as_bytes();
        let tb = t.as_bytes();
        for i in 0..sb.len() {
            let a = (sb[i] - b'a') as i32;
            let b = (tb[i] - b'a') as i32;
            if a == b {
                continue;
            }
            let mut fwd = 0i64;
            let mut x = a;
            while x != b {
                fwd += next_cost[x as usize] as i64;
                x = (x + 1) % 26;
            }
            let mut bwd = 0i64;
            let mut x = a;
            while x != b {
                bwd += previous_cost[x as usize] as i64;
                x = (x + 25) % 26;
            }
            ans += if fwd < bwd { fwd } else { bwd };
        }
        ans
    }
}

fn main() {}
