// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

impl Solution {
    pub fn max_value(n: i32, restrictions: Vec<Vec<i32>>, diff: Vec<i32>) -> i32 {
        const INF: i32 = i32::MAX / 4;
        let n = n as usize;
        let mut bound = vec![INF; n];
        bound[0] = 0;
        for r in &restrictions {
            bound[r[0] as usize] = r[1];
        }
        for i in 1..n {
            bound[i] = bound[i].min(bound[i - 1] + diff[i - 1]);
        }
        for i in (0..n - 1).rev() {
            bound[i] = bound[i].min(bound[i + 1] + diff[i]);
        }
        *bound.iter().max().unwrap()
    }
}
