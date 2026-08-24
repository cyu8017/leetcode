// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

impl Solution {
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_unstable();
        let mut ans = 0i64;
        let n = happiness.len();
        for i in 0..k {
            let x = happiness[n - i as usize - 1] - i;
            ans += x.max(0) as i64;
        }
        ans
    }
}
