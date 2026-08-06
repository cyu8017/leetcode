// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

impl Solution {
    pub fn process_queries(queries: Vec<i32>, m: i32) -> Vec<i32> {
        let mut values: Vec<i32> = (1..=m).collect();
        let mut answer = Vec::new();
        for query in queries {
            let index = values.iter().position(|&v| v == query).unwrap();
            answer.push(index as i32);
            let v = values.remove(index);
            values.insert(0, v);
        }
        answer
    }
}
