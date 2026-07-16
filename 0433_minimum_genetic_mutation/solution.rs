// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_mutation(start_gene: String, end_gene: String, bank: Vec<String>) -> i32 {
        if start_gene == end_gene {
            return 0;
        }

        let valid: HashSet<String> = bank.into_iter().collect();
        if !valid.contains(&end_gene) {
            return -1;
        }

        let genes = ['A', 'C', 'G', 'T'];
        let mut queue = VecDeque::new();
        let mut visited = HashSet::new();
        queue.push_back((start_gene.clone(), 0));
        visited.insert(start_gene);

        while let Some((gene, steps)) = queue.pop_front() {
            if gene == end_gene {
                return steps;
            }

            let mut chars: Vec<char> = gene.chars().collect();
            for index in 0..chars.len() {
                let original = chars[index];
                for letter in genes {
                    if letter == original {
                        continue;
                    }
                    chars[index] = letter;
                    let candidate: String = chars.iter().collect();
                    if valid.contains(&candidate) && visited.insert(candidate.clone()) {
                        queue.push_back((candidate, steps + 1));
                    }
                }
                chars[index] = original;
            }
        }

        -1
    }
}
