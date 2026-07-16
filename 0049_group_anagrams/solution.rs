// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();

        for word in &strs {
            let mut key: Vec<char> = word.chars().collect();
            key.sort_unstable();
            let key: String = key.into_iter().collect();
            groups.entry(key).or_default().push(word.clone());
        }

        let mut result: Vec<Vec<String>> = groups.into_values().collect();
        for group in &mut result {
            group.sort_unstable();
        }
        result.sort_by(|a, b| min_group_index(&strs, b).cmp(&min_group_index(&strs, a)));
        result
    }

    fn min_group_index(strs: &[String], group: &[String]) -> usize {
        group
            .iter()
            .map(|word| strs.iter().position(|candidate| candidate == word).unwrap())
            .min()
            .unwrap()
    }
}
