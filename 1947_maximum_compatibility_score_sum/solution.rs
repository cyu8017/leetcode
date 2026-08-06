// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

use std::collections::HashMap;

impl Solution {
    pub fn max_compatibility_sum(students: Vec<Vec<i32>>, mentors: Vec<Vec<i32>>) -> i32 {
        let m = students.len();
        let mut score = vec![vec![0; m]; m];
        for i in 0..m {
            for j in 0..m {
                score[i][j] = students[i]
                    .iter()
                    .zip(mentors[j].iter())
                    .filter(|(a, b)| a == b)
                    .count() as i32;
            }
        }

        let mut memo: HashMap<(usize, i32), i32> = HashMap::new();

        fn dp(
            i: usize,
            mask: i32,
            m: usize,
            score: &[Vec<i32>],
            memo: &mut HashMap<(usize, i32), i32>,
        ) -> i32 {
            if i == m {
                return 0;
            }
            if let Some(&v) = memo.get(&(i, mask)) {
                return v;
            }
            let mut best = 0;
            for j in 0..m {
                if mask & (1 << j) == 0 {
                    best = best.max(score[i][j] + dp(i + 1, mask | (1 << j), m, score, memo));
                }
            }
            memo.insert((i, mask), best);
            best
        }

        dp(0, 0, m, &score, &mut memo)
    }
}
