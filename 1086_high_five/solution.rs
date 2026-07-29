// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

use std::collections::BTreeMap;

impl Solution {
    pub fn high_five(items: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut scores: BTreeMap<i32, Vec<i32>> = BTreeMap::new();
        for item in &items {
            scores.entry(item[0]).or_default().push(item[1]);
        }
        let mut ans = Vec::new();
        for (student_id, mut score_list) in scores {
            score_list.sort_unstable_by(|a, b| b.cmp(a));
            let top: i32 = score_list.iter().take(5).sum();
            ans.push(vec![student_id, top / 5]);
        }
        ans
    }
}
