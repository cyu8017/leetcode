struct Solution;
// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

impl Solution {
    pub fn number_of_ways(n: i32, m: i32, k: i32, source: Vec<i32>, dest: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let sx = source[0];
        let sy = source[1];
        let tx = dest[0];
        let ty = dest[1];
        let mut same = 0i64;
        let mut row = 0i64;
        let mut col = 0i64;
        let mut other = 0i64;
        if sx == tx && sy == ty {
            same = 1;
        } else if sx == tx {
            row = 1;
        } else if sy == ty {
            col = 1;
        } else {
            other = 1;
        }
        let n = n as i64;
        let m = m as i64;
        for _ in 0..k {
            let ns = (row * (m - 1) + col * (n - 1)) % MOD;
            let nr = (same + row * (m - 2) % MOD + other * (n - 1) % MOD) % MOD;
            let nc = (same + col * (n - 2) % MOD + other * (m - 1) % MOD) % MOD;
            let no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % MOD) % MOD;
            same = ns;
            row = nr;
            col = nc;
            other = no;
        }
        if sx == tx && sy == ty {
            same as i32
        } else if sx == tx {
            row as i32
        } else if sy == ty {
            col as i32
        } else {
            other as i32
        }
    }
}

fn main() {}
