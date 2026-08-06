// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

use std::collections::HashMap;

impl Solution {
    pub fn generate_sentences(synonyms: Vec<Vec<String>>, text: String) -> Vec<String> {
        let mut parent: HashMap<String, String> = HashMap::new();
        fn find(parent: &mut HashMap<String, String>, x: &str) -> String {
            if !parent.contains_key(x) {
                parent.insert(x.to_string(), x.to_string());
            }
            let p = parent[x].clone();
            if p != x {
                let r = find(parent, &p);
                parent.insert(x.to_string(), r.clone());
                r
            } else {
                p
            }
        }
        for pair in &synonyms {
            let a = find(&mut parent, &pair[0]);
            let b = find(&mut parent, &pair[1]);
            parent.insert(a, b);
        }
        let words_keys: Vec<String> = parent.keys().cloned().collect();
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();
        for word in words_keys {
            let r = find(&mut parent, &word);
            groups.entry(r).or_default().push(word);
        }
        for g in groups.values_mut() {
            g.sort();
        }
        let words: Vec<&str> = text.split_whitespace().collect();
        let choices: Vec<Vec<String>> = words
            .iter()
            .map(|w| {
                if parent.contains_key(*w) {
                    groups[&find(&mut parent, w)].clone()
                } else {
                    vec![(*w).to_string()]
                }
            })
            .collect();
        let mut ans = Vec::new();
        fn dfs(i: usize, cur: &mut Vec<String>, choices: &[Vec<String>], ans: &mut Vec<String>) {
            if i == choices.len() {
                ans.push(cur.join(" "));
                return;
            }
            for w in &choices[i] {
                cur.push(w.clone());
                dfs(i + 1, cur, choices, ans);
                cur.pop();
            }
        }
        dfs(0, &mut Vec::new(), &choices, &mut ans);
        ans
    }
}
