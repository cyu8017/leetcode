// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

impl Solution {
    pub fn max_satisfaction(mut satisfaction: Vec<i32>) -> i32 {
        satisfaction.sort_unstable_by(|a, b| b.cmp(a));
        let mut total = 0;
        let mut answer = 0;
        for value in satisfaction {
            if total + value <= 0 {
                break;
            }
            total += value;
            answer += total;
        }
        answer
    }
}
