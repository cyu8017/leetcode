// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

use std::collections::HashMap;

impl Solution {
    pub fn are_sentences_similar_two(
        sentence1: Vec<String>,
        sentence2: Vec<String>,
        similar_pairs: Vec<Vec<String>>,
    ) -> bool {
        if sentence1.len() != sentence2.len() {
            return false;
        }
        let mut parent = HashMap::new();
        for pair in similar_pairs {
            Self::unite(&mut parent, &pair[0], &pair[1]);
        }
        for (a, b) in sentence1.iter().zip(sentence2.iter()) {
            if Self::find(&mut parent, a) != Self::find(&mut parent, b) {
                return false;
            }
        }
        true
    }

    fn find(parent: &mut HashMap<String, String>, x: &str) -> String {
        parent.entry(x.to_string()).or_insert_with(|| x.to_string());
        let mut cur = x.to_string();
        while parent[&cur] != cur {
            let grand = parent[&parent[&cur]].clone();
            parent.insert(cur.clone(), grand);
            cur = parent[&cur].clone();
        }
        cur
    }

    fn unite(parent: &mut HashMap<String, String>, a: &str, b: &str) {
        let pa = Self::find(parent, a);
        let pb = Self::find(parent, b);
        parent.insert(pa, pb);
    }
}
