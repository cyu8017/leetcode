// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

impl Solution {
    pub fn min_moves(balance: Vec<i32>) -> i64 {
        let mut sum = 0i64;
        for &b in &balance {
            sum += b as i64;
        }
        if sum < 0 {
            return -1;
        }
        let n = balance.len();
        let mut mn = balance[0];
        let mut idx = 0usize;
        for i in 1..n {
            if balance[i] < mn {
                mn = balance[i];
                idx = i;
            }
        }
        if mn >= 0 {
            return 0;
        }
        let mut need = -mn;
        let mut ans = 0i64;
        for j in 1..n {
            let a = balance[(idx + n - j) % n];
            let b = balance[(idx + j) % n];
            let c1 = a.min(need);
            need -= c1;
            ans += c1 as i64 * j as i64;
            let c2 = b.min(need);
            need -= c2;
            ans += c2 as i64 * j as i64;
        }
        ans
    }
}
