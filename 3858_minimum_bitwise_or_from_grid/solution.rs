// LeetCode 3858 - Minimum Bitwise OR From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

impl Solution {
    pub fn minimum_or(grid: Vec<Vec<i32>>) -> i32 {
        let mx = grid.iter().flat_map(|row| row.iter()).copied().max().unwrap_or(0);
        let m = if mx == 0 { 0 } else { 32 - (mx as u32).leading_zeros() as i32 };
        let mut ans = 0;
        for i in (0..m).rev() {
            let mask = ans | ((1 << i) - 1);
            let mut found_all = true;
            for row in &grid {
                let found = row.iter().any(|&x| (x | mask) == mask);
                if !found {
                    ans |= 1 << i;
                    found_all = false;
                    break;
                }
            }
            let _ = found_all;
        }
        ans
    }
}
