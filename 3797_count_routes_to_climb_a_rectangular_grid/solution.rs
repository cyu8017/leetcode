// LeetCode 3797 - Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

impl Solution {
    pub fn count_routes(grid: Vec<String>, d: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = grid.len();
        let m = grid[0].len();
        let grid: Vec<Vec<u8>> = grid.into_iter().map(|s| s.into_bytes()).collect();
        let mut up_radius = 0;
        while (up_radius + 1) * (up_radius + 1) + 1 <= d * d {
            up_radius += 1;
        }
        let mut arrived = vec![0i32; m];
        for c in 0..m {
            if grid[n - 1][c] == b'.' {
                arrived[c] = 1;
            }
        }
        let row_ways = |row: usize, base: &[i32]| -> (Vec<i32>, Vec<i32>) {
            let mut pref = vec![0i32; m + 1];
            for i in 0..m {
                pref[i + 1] = (pref[i] + base[i]) % MOD;
            }
            let mut horizontal = vec![0i32; m];
            for c in 0..m {
                if grid[row][c] == b'#' {
                    continue;
                }
                let l = 0.max(c as i32 - d) as usize;
                let r = (m as i32 - 1).min(c as i32 + d) as usize;
                horizontal[c] = (pref[r + 1] - pref[l] - base[c]) % MOD;
                if horizontal[c] < 0 {
                    horizontal[c] += MOD;
                }
            }
            (base.to_vec(), horizontal)
        };
        for r in (0..n).rev() {
            let (base, horizontal) = row_ways(r, &arrived);
            if r == 0 {
                let mut ans = 0;
                for c in 0..m {
                    ans = (ans + base[c] + horizontal[c]) % MOD;
                }
                return ans;
            }
            let mut pref = vec![0i32; m + 1];
            for c in 0..m {
                pref[c + 1] = (pref[c] + base[c] + horizontal[c]) % MOD;
            }
            let mut next = vec![0i32; m];
            for c in 0..m {
                if grid[r - 1][c] == b'#' {
                    continue;
                }
                let l = 0.max(c as i32 - up_radius) as usize;
                let rr = (m as i32 - 1).min(c as i32 + up_radius) as usize;
                next[c] = pref[rr + 1] - pref[l];
                if next[c] < 0 {
                    next[c] += MOD;
                }
            }
            arrived = next;
        }
        0
    }
}
