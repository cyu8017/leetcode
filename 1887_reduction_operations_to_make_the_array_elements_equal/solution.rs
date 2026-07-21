// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

impl Solution {
    pub fn reduction_operations(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut answer = 0;
        let mut rank = 0;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                rank += 1;
            }
            answer += rank;
        }
        answer
    }
}
