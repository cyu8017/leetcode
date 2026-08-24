// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

impl Solution {
    pub fn number_of_permutations(n: i32, requirements: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut req = vec![-1; n];
        for r in &requirements {
            req[r[0] as usize] = r[1];
        }
        if req[0] > 0 {
            return 0;
        }
        req[0] = 0;
        let m = *req.iter().max().unwrap() as usize;
        const MOD: i32 = 1_000_000_007;
        let mut f = vec![vec![0; m + 1]; n];
        f[0][0] = 1;
        for i in 1..n {
            let (mut l, mut r) = (0, m as i32);
            if req[i] >= 0 {
                l = req[i];
                r = req[i];
            }
            for j in l..=r {
                let j = j as usize;
                for k in 0..=i.min(j) {
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % MOD;
                }
            }
        }
        f[n - 1][req[n - 1] as usize]
    }
}
