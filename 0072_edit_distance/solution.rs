// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let m = word1.len();
        let n = word2.len();
        let w1: Vec<char> = word1.chars().collect();
        let w2: Vec<char> = word2.chars().collect();
        let mut prev: Vec<i32> = (0..=n as i32).collect();
        let mut curr = vec![0; n + 1];

        for i in 1..=m {
            curr[0] = i as i32;
            for j in 1..=n {
                if w1[i - 1] == w2[j - 1] {
                    curr[j] = prev[j - 1];
                } else {
                    curr[j] = 1 + prev[j].min(curr[j - 1]).min(prev[j - 1]);
                }
            }
            std::mem::swap(&mut prev, &mut curr);
        }

        prev[n]
    }
}
