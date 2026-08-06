// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

impl Solution {
    pub fn build_array(target: Vec<i32>, _n: i32) -> Vec<String> {
        let mut answer = Vec::new();
        let mut current = 1;
        for value in target {
            while current < value {
                answer.push("Push".to_string());
                answer.push("Pop".to_string());
                current += 1;
            }
            answer.push("Push".to_string());
            current += 1;
        }
        answer
    }
}
