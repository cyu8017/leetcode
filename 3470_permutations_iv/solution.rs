// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

impl Solution {
    pub fn permute(n: i32, mut k: i64) -> Vec<i32> {
        let n = n as usize;
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1].saturating_mul(i as i64);
            if fact[i] > 1e18 as i64 {
                fact[i] = 1e18 as i64 + 1;
            }
        }
        let mut used = vec![false; n + 1];
        let mut ans = Vec::new();
        fn dfs(
            pos: usize,
            n: usize,
            k: &mut i64,
            fact: &[i64],
            used: &mut [bool],
            ans: &mut Vec<i32>,
        ) -> bool {
            if pos == n {
                return true;
            }
            for x in 1..=n as i32 {
                if used[x as usize] {
                    continue;
                }
                if pos > 0 && ans[pos - 1] % 2 == x % 2 {
                    continue;
                }
                let rem = n - pos - 1;
                let cnt = fact[rem];
                if cnt >= *k {
                    used[x as usize] = true;
                    ans.push(x);
                    if dfs(pos + 1, n, k, fact, used, ans) {
                        return true;
                    }
                    ans.pop();
                    used[x as usize] = false;
                } else {
                    *k -= cnt;
                }
            }
            false
        }
        if !dfs(0, n, &mut k, &fact, &mut used, &mut ans) {
            return vec![];
        }
        ans
    }
}
