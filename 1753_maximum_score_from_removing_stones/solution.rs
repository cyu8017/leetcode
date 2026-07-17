// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

impl Solution {
    pub fn maximum_score(a: i32, b: i32, c: i32) -> i32 {
        let mut stones = vec![a, b, c];
        stones.sort_unstable_by(|x, y| y.cmp(x));
        let mut score = 0;
        while stones[0] > 0 && stones[1] > 0 {
            stones[0] -= 1;
            stones[1] -= 1;
            score += 1;
            stones.sort_unstable_by(|x, y| y.cmp(x));
        }
        score
    }
}
