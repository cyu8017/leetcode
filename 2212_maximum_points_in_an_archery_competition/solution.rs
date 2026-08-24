// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

impl Solution {
    pub fn maximum_bob_points(num_arrows: i32, alice_arrows: Vec<i32>) -> Vec<i32> {
        let mut best_score = -1;
        let mut best = vec![0; 12];
        fn dfs(
            i: usize,
            remain: i32,
            score: i32,
            bob: &mut [i32],
            alice: &[i32],
            best_score: &mut i32,
            best: &mut [i32],
        ) {
            if i == 12 {
                if score > *best_score {
                    *best_score = score;
                    best.copy_from_slice(bob);
                    if remain > 0 {
                        best[0] += remain;
                    }
                }
                return;
            }
            dfs(i + 1, remain, score, bob, alice, best_score, best);
            let need = alice[i] + 1;
            if remain >= need {
                bob[i] = need;
                dfs(i + 1, remain - need, score + i as i32, bob, alice, best_score, best);
                bob[i] = 0;
            }
        }
        let mut bob = vec![0; 12];
        dfs(0, num_arrows, 0, &mut bob, &alice_arrows, &mut best_score, &mut best);
        best
    }
}
