// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

impl Solution {
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let sum: i32 = rolls.iter().sum();
        let remain = mean * (rolls.len() as i32 + n) - sum;
        if remain < n || remain > 6 * n {
            return vec![];
        }
        let mut ans = vec![remain / n; n as usize];
        let extra = remain % n;
        for i in 0..extra as usize {
            ans[i] += 1;
        }
        ans
    }
}
