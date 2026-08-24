// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

impl Solution {
    pub fn number_of_arrays(differences: Vec<i32>, lower: i32, upper: i32) -> i32 {
        let mut cur = 0i64;
        let mut mn = 0i64;
        let mut mx = 0i64;
        for d in differences {
            cur += d as i64;
            mn = mn.min(cur);
            mx = mx.max(cur);
        }
        let res = (upper as i64 - lower as i64) - (mx - mn) + 1;
        if res < 0 { 0 } else { res as i32 }
    }
}
