// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

impl Solution {
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
        let n = code.len();
        if k == 0 {
            return vec![0; n];
        }
        let a: Vec<i32> = code.iter().chain(code.iter()).copied().collect();
        let mut ans = Vec::with_capacity(n);
        for i in 0..n {
            if k > 0 {
                ans.push(a[i + 1..i + 1 + k as usize].iter().sum());
            } else {
                let kk = (-k) as usize;
                ans.push(a[i + n - kk..i + n].iter().sum());
            }
        }
        ans
    }
}
