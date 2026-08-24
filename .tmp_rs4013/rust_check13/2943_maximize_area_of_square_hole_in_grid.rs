#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

impl Solution {
    pub fn maximize_square_hole_area(_n: i32, _m: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        fn max_gap(mut bars: Vec<i32>) -> i32 {
            if bars.is_empty() {
                return 1;
            }
            bars.sort_unstable();
            let mut best = 1;
            let mut cur = 1;
            for i in 1..bars.len() {
                if bars[i] == bars[i - 1] + 1 {
                    cur += 1;
                } else {
                    cur = 1;
                }
                if cur > best {
                    best = cur;
                }
            }
            best + 1
        }
        let mut side = max_gap(h_bars);
        let vs = max_gap(v_bars);
        if vs < side {
            side = vs;
        }
        side * side
    }
}
