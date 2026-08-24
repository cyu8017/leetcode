struct Solution;
// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

impl Solution {
    pub fn max_score(points: Vec<i32>, m: i32) -> i64 {
        let ok = |mid: i64| -> bool {
            let mut need = 0i64;
            let mut extra = 0i64;
            for &p in &points {
                let req = (mid + p as i64 - 1) / p as i64;
                if req > extra {
                    let visits = req - extra;
                    need += 2 * visits - 1;
                    extra = visits - 1;
                } else {
                    need += 1;
                    extra = 0;
                }
                if need > m as i64 {
                    return false;
                }
            }
            need <= m as i64
        };
        let mut lo = 0i64;
        let mut hi = 1e18 as i64;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}

fn main() {}
