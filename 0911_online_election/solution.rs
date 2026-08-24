// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

use std::collections::HashMap;

pub struct TopVotedCandidate {
    times: Vec<i32>,
    leaders: Vec<i32>,
}

impl TopVotedCandidate {
    pub fn new(persons: Vec<i32>, times: Vec<i32>) -> Self {
        let mut counts = HashMap::new();
        let mut leader = -1;
        let mut leaders = vec![0; persons.len()];
        for (i, &p) in persons.iter().enumerate() {
            *counts.entry(p).or_insert(0) += 1;
            if leader == -1 || counts[&p] >= counts[&leader] {
                leader = p;
            }
            leaders[i] = leader;
        }
        Self { times, leaders }
    }

    pub fn q(&self, t: i32) -> i32 {
        let i = self.times.partition_point(|&x| x <= t) as i32 - 1;
        self.leaders[i as usize]
    }
}
