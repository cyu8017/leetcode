struct Solution;
// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

use std::collections::HashMap;

impl Solution {
    fn unique_mode(a: &[i32]) -> bool {
        let mut freq = HashMap::new();
        for &x in a {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut best = 0;
        let mut cnt = 0;
        for &f in freq.values() {
            if f > best {
                best = f;
                cnt = 1;
            } else if f == best {
                cnt += 1;
            }
        }
        cnt == 1
    }

    pub fn subsequences_with_middle_mode(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let mut ans = 0;
        for mid in 2..n.saturating_sub(2) {
            for a in 0..mid {
                for b in (a + 1)..mid {
                    for c in (mid + 1)..n {
                        for d in (c + 1)..n {
                            let seq = [nums[a], nums[b], nums[mid], nums[c], nums[d]];
                            if Self::unique_mode(&seq) {
                                ans = (ans + 1) % MOD;
                            }
                        }
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
