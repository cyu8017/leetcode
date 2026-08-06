// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

use std::collections::HashMap;

impl Solution {
    pub fn get_folder_names(names: Vec<String>) -> Vec<String> {
        let mut used: HashMap<String, i32> = HashMap::new();
        let mut ans = Vec::new();
        for name in names {
            let candidate = if !used.contains_key(&name) {
                name.clone()
            } else {
                let mut k = used[&name];
                let mut cand = format!("{}({})", name, k);
                while used.contains_key(&cand) {
                    k += 1;
                    cand = format!("{}({})", name, k);
                }
                used.insert(name.clone(), k + 1);
                cand
            };
            used.insert(candidate.clone(), 1);
            ans.push(candidate);
        }
        ans
    }
}
