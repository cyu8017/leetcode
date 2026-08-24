// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

impl Solution {
    pub fn max_div_score(nums: Vec<i32>, divisors: Vec<i32>) -> i32 {
        let mut best = divisors[0];
        let mut best_score = -1;
        for d in divisors {
            let mut score = 0;
            for &x in &nums {
                if x % d == 0 {
                    score += 1;
                }
            }
            if score > best_score || (score == best_score && d < best) {
                best_score = score;
                best = d;
            }
        }
        best
    }
}
