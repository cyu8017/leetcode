// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

impl Solution {
    pub fn count_non_adjacent_subsets(parent: Vec<i32>, nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = parent.len();
        let k = k as usize;
        let mut children = vec![Vec::new(); n];
        for i in 1..n {
            children[parent[i] as usize].push(i);
        }
        let mut dp0 = vec![Vec::new(); n];
        let mut dp1 = vec![Vec::new(); n];
        for u in (0..n).rev() {
            let mut a = vec![0i64; k];
            let mut b = vec![0i64; k];
            a[0] = 1;
            b[(((nums[u] % k as i32) + k as i32) % k as i32) as usize] = 1;
            for &v in &children[u] {
                let mut na = vec![0i64; k];
                let mut nb = vec![0i64; k];
                for x in 0..k {
                    for y in 0..k {
                        let all_child = (dp0[v][y] + dp1[v][y]) % MOD;
                        na[(x + y) % k] = (na[(x + y) % k] + a[x] * all_child) % MOD;
                        nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % MOD;
                    }
                }
                a = na;
                b = nb;
            }
            dp0[u] = a;
            dp1[u] = b;
        }
        let mut ans = (dp0[0][0] + dp1[0][0] - 1) % MOD;
        if ans < 0 {
            ans += MOD;
        }
        ans as i32
    }
}
