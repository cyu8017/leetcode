// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

use std::collections::HashMap;

impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut pending: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut answer = Vec::new();
        for (person, &size) in group_sizes.iter().enumerate() {
            let group = pending.entry(size).or_default();
            group.push(person as i32);
            if group.len() == size as usize {
                answer.push(group.clone());
                group.clear();
            }
        }
        answer.sort_by(|a, b| a.len().cmp(&b.len()).then_with(|| a.cmp(b)));
        answer
    }
}
