// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn alien_order(words: Vec<String>) -> String {
        let mut graph: HashMap<char, HashSet<char>> = HashMap::new();
        let mut indegree: HashMap<char, i32> = HashMap::new();

        for word in &words {
            for ch in word.chars() {
                graph.entry(ch).or_insert_with(HashSet::new);
                indegree.entry(ch).or_insert(0);
            }
        }

        for index in 0..words.len().saturating_sub(1) {
            let first = words[index].as_str();
            let second = words[index + 1].as_str();
            if first.len() > second.len() && first.starts_with(second) {
                return String::new();
            }
            let limit = first.len().min(second.len());
            let mut pair_found = false;
            for (left, right) in first.chars().zip(second.chars()).take(limit) {
                if left != right {
                    let neighbors = graph.entry(left).or_insert_with(HashSet::new);
                    if neighbors.insert(right) {
                        *indegree.entry(right).or_insert(0) += 1;
                    }
                    pair_found = true;
                    break;
                }
            }
            let _ = pair_found;
        }

        let mut queue = VecDeque::new();
        for (&ch, &degree) in &indegree {
            if degree == 0 {
                queue.push_back(ch);
            }
        }

        let mut order = String::new();
        while let Some(ch) = queue.pop_front() {
            order.push(ch);
            if let Some(neighbors) = graph.get(&ch).cloned() {
                for next in neighbors {
                    if let Some(entry) = indegree.get_mut(&next) {
                        *entry -= 1;
                        if *entry == 0 {
                            queue.push_back(next);
                        }
                    }
                }
            }
        }

        if order.chars().count() == indegree.len() {
            order
        } else {
            String::new()
        }
    }
}
