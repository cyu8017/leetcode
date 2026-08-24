// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

use std::collections::HashMap;

impl Solution {
    pub fn num_rabbits(answers: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();
        for answer in answers {
            *counts.entry(answer).or_insert(0) += 1;
        }
        let mut total = 0;
        for (answer, count) in counts {
            let group = answer + 1;
            let groups = (count + group - 1) / group;
            total += groups * group;
        }
        total
    }
}
