// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

impl Solution {
    pub fn max_possible_score(mut start: Vec<i32>, d: i32) -> i32 {
        start.sort_unstable();
        let n = start.len();
        let ok = |mid: i32| -> bool {
            let mut prev = start[0] as i64;
            for i in 1..n {
                let need = prev + mid as i64;
                let cur = start[i] as i64;
                if need > cur + d as i64 {
                    return false;
                }
                prev = if need > cur { need } else { cur };
            }
            true
        };
        let mut lo = 0;
        let mut hi = start[n - 1] + d - start[0] + 1;
        while lo < hi {
            let mid = (lo as i64 + hi as i64 + 1) / 2;
            let mid = mid as i32;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
