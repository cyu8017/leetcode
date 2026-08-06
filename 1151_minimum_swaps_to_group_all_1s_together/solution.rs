// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

impl Solution {
    pub fn min_swaps(data: Vec<i32>) -> i32 {
        let ones: i32 = data.iter().sum();
        if ones <= 1 {
            return 0;
        }
        let ones = ones as usize;
        let mut cur: i32 = data[..ones].iter().sum();
        let mut best = cur;
        for i in ones..data.len() {
            cur += data[i] - data[i - ones];
            best = best.max(cur);
        }
        ones as i32 - best
    }
}
