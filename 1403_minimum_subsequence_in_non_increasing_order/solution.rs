// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

impl Solution {
    pub fn min_subsequence(mut nums: Vec<i32>) -> Vec<i32> {
        let total: i32 = nums.iter().sum();
        nums.sort_unstable_by(|a, b| b.cmp(a));
        let mut answer = Vec::new();
        let mut chosen = 0;
        for value in nums {
            answer.push(value);
            chosen += value;
            if chosen > total - chosen {
                return answer;
            }
        }
        answer
    }
}
