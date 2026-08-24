struct Solution;
// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

impl Solution {
    pub fn max_total_reward(mut reward_values: Vec<i32>) -> i32 {
        reward_values.sort_unstable();
        reward_values.dedup();
        const N: usize = 100001;
        let mut f = vec![false; N];
        f[0] = true;
        for &v in &reward_values {
            let v = v as usize;
            let mut mask = f.clone();
            for i in v..N {
                mask[i] = false;
            }
            for i in 0..N {
                if mask[i] && i + v < N {
                    f[i + v] = true;
                }
            }
        }
        for i in (0..N).rev() {
            if f[i] {
                return i as i32;
            }
        }
        0
    }
}

fn main() {}
