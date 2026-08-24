// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

impl Solution {
    pub fn judge_point24(cards: Vec<i32>) -> bool {
        let nums: Vec<f64> = cards.into_iter().map(|c| c as f64).collect();
        Self::dfs(nums)
    }

    fn dfs(nums: Vec<f64>) -> bool {
        const EPS: f64 = 1e-6;
        if nums.len() == 1 {
            return (nums[0] - 24.0).abs() < EPS;
        }
        for i in 0..nums.len() {
            for j in 0..nums.len() {
                if i == j {
                    continue;
                }
                let mut rest: Vec<f64> = nums
                    .iter()
                    .enumerate()
                    .filter(|(k, _)| *k != i && *k != j)
                    .map(|(_, v)| *v)
                    .collect();
                let a = nums[i];
                let b = nums[j];
                let mut candidates = vec![a + b, a - b, a * b];
                if b.abs() > EPS {
                    candidates.push(a / b);
                }
                for value in candidates {
                    rest.push(value);
                    if Self::dfs(rest.clone()) {
                        return true;
                    }
                    rest.pop();
                }
            }
        }
        false
    }
}
