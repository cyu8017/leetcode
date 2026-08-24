// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_points(s: String, k: i32) -> i32 {
        let n = s.len();
        let k = k as usize;
        let bytes = s.as_bytes();
        let mut f = vec![0i32; n + 1];
        let mut g = vec![0i32; n + 1];
        let mut x = 0;
        let mut y = 0;
        for i in 1..=n {
            match bytes[i - 1] {
                b'U' => y += 1,
                b'D' => y -= 1,
                b'L' => x -= 1,
                _ => x += 1,
            }
            f[i] = x;
            g[i] = y;
        }
        let mut st = HashSet::new();
        for i in k..=n {
            let a = f[n] - (f[i] - f[i - k]);
            let b = g[n] - (g[i] - g[i - k]);
            let key = a as i64 * n as i64 + b as i64;
            st.insert(key);
        }
        st.len() as i32
    }
}
