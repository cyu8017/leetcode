// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

impl Solution {
    pub fn total_score(hp: i32, damage: Vec<i32>, requirement: Vec<i32>) -> i64 {
        let n = damage.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + damage[i] as i64;
        }
        let mut answer = n as i64 * (n as i64 + 1) / 2;
        for j in 1..=n {
            let threshold = prefix[j] + (requirement[j - 1] - hp) as i64;
            let invalid = prefix[..j].partition_point(|&v| v < threshold);
            answer -= invalid as i64;
        }
        answer
    }
}
