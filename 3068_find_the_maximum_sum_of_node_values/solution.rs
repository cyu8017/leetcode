// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, _edges: Vec<Vec<i32>>) -> i64 {
        let mut f0 = 0i64;
        let mut f1 = -0x3f3f3f3fi64;
        for x in nums {
            let x = x as i64;
            let xk = (x as i32 ^ k) as i64;
            let nf0 = (f0 + x).max(f1 + xk);
            let nf1 = (f1 + x).max(f0 + xk);
            f0 = nf0;
            f1 = nf1;
        }
        f0
    }
}
