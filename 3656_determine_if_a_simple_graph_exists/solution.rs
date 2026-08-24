// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

impl Solution {
    pub fn simple_graph_exists(degrees: Vec<i32>) -> bool {
        let n = degrees.len();
        let mut d = degrees;
        d.sort_unstable_by(|a, b| b.cmp(a));
        let mut sum = 0i64;
        for &x in &d {
            if x < 0 || x >= n as i32 {
                return false;
            }
            sum += x as i64;
        }
        if sum % 2 == 1 {
            return false;
        }
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + d[i] as i64;
        }
        for k in 1..=n {
            let mut right = 0i64;
            for i in k..n {
                right += if d[i] < k as i32 { d[i] as i64 } else { k as i64 };
            }
            if prefix[k] > k as i64 * (k as i64 - 1) + right {
                return false;
            }
        }
        true
    }
}
