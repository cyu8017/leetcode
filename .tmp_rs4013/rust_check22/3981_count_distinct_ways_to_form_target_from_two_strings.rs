struct Solution;
// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

impl Solution {
    pub fn count_ways(word1: String, word2: String, target: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let word1 = word1.into_bytes();
        let word2 = word2.into_bytes();
        let n1 = word1.len();
        let n2 = word2.len();
        let size = (n1 + 1) * (n2 + 1) * 4;
        let index = |i: usize, j: usize, mask: usize| ((i * (n2 + 1) + j) * 4) + mask;
        let mut dp = vec![0i32; size];
        let mut next = vec![0i32; size];
        dp[index(0, 0, 0)] = 1;
        for ch in target.bytes() {
            next.fill(0);
            for j in 0..=n2 {
                let mut prefix = [0i32; 4];
                for a in 0..n1 {
                    for mask in 0..4 {
                        prefix[mask] += dp[index(a, j, mask)];
                        if prefix[mask] >= MOD {
                            prefix[mask] -= MOD;
                        }
                    }
                    if word1[a] == ch {
                        for mask in 0..4 {
                            let at = index(a + 1, j, mask | 1);
                            next[at] += prefix[mask];
                            if next[at] >= MOD {
                                next[at] -= MOD;
                            }
                        }
                    }
                }
            }
            for i in 0..=n1 {
                let mut prefix = [0i32; 4];
                for b in 0..n2 {
                    for mask in 0..4 {
                        prefix[mask] += dp[index(i, b, mask)];
                        if prefix[mask] >= MOD {
                            prefix[mask] -= MOD;
                        }
                    }
                    if word2[b] == ch {
                        for mask in 0..4 {
                            let at = index(i, b + 1, mask | 2);
                            next[at] += prefix[mask];
                            if next[at] >= MOD {
                                next[at] -= MOD;
                            }
                        }
                    }
                }
            }
            std::mem::swap(&mut dp, &mut next);
        }
        let mut answer = 0;
        for i in 0..=n1 {
            for j in 0..=n2 {
                answer += dp[index(i, j, 3)];
                if answer >= MOD {
                    answer -= MOD;
                }
            }
        }
        answer
    }
}

fn main() {}
