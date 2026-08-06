// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

use std::collections::HashMap;

impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = m as usize;
        let n = n as usize;

        fn valid_column(mut mask: i32, m: usize) -> bool {
            let mut prev = -1;
            for _ in 0..m {
                let c = mask % 3;
                if c == prev {
                    return false;
                }
                prev = c;
                mask /= 3;
            }
            true
        }

        fn get_colors(mut mask: i32, m: usize) -> Vec<i32> {
            let mut cols = Vec::with_capacity(m);
            for _ in 0..m {
                cols.push(mask % 3);
                mask /= 3;
            }
            cols
        }

        let total = 3i32.pow(m as u32);
        let states: Vec<i32> = (0..total).filter(|&s| valid_column(s, m)).collect();
        let mut compat: HashMap<i32, Vec<i32>> = HashMap::new();
        for &a in &states {
            let ca = get_colors(a, m);
            let mut ok = Vec::new();
            for &b in &states {
                let cb = get_colors(b, m);
                if ca.iter().zip(cb.iter()).all(|(x, y)| x != y) {
                    ok.push(b);
                }
            }
            compat.insert(a, ok);
        }

        let mut memo: HashMap<(usize, i32), i32> = HashMap::new();

        fn dp(
            col: usize,
            prev: i32,
            n: usize,
            states: &[i32],
            compat: &HashMap<i32, Vec<i32>>,
            memo: &mut HashMap<(usize, i32), i32>,
        ) -> i32 {
            if col == n {
                return 1;
            }
            if let Some(&v) = memo.get(&(col, prev)) {
                return v;
            }
            let mut total = 0i32;
            let candidates: &[i32] = if prev == -1 {
                states
            } else {
                &compat[&prev]
            };
            for &cur in candidates {
                total = (total + dp(col + 1, cur, n, states, compat, memo)) % MOD;
            }
            memo.insert((col, prev), total);
            total
        }

        dp(0, -1, n, &states, &compat, &mut memo)
    }
}
