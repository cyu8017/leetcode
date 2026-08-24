// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

impl Solution {
    pub fn min_increments(n: i32, mut cost: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut i = n / 2 - 1;
        while i >= 0 {
            let l = (2 * i + 1) as usize;
            let r = (2 * i + 2) as usize;
            ans += (cost[l] - cost[r]).abs();
            cost[i as usize] += cost[l].max(cost[r]);
            i -= 1;
        }
        ans
    }
}
