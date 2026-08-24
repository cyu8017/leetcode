// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

impl Solution {
    pub fn number_of_nodes(n: i32, queries: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut flip = vec![0; n + 1];
        let mut val = vec![0; n + 1];
        for q in queries {
            flip[q as usize] ^= 1;
        }
        let mut ans = 0;
        for i in 1..=n {
            val[i] = flip[i];
            if i > 1 {
                val[i] ^= val[i / 2];
            }
            ans += val[i];
        }
        ans
    }
}
