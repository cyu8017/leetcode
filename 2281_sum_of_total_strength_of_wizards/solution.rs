// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

impl Solution {
    pub fn total_strength(strength: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = strength.len();
        let mut left = vec![0i32; n];
        let mut right = vec![0i32; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while !stack.is_empty() && strength[*stack.last().unwrap()] >= strength[i] {
                stack.pop();
            }
            left[i] = if stack.is_empty() { -1 } else { *stack.last().unwrap() as i32 };
            stack.push(i);
        }
        stack.clear();
        for i in (0..n).rev() {
            while !stack.is_empty() && strength[*stack.last().unwrap()] > strength[i] {
                stack.pop();
            }
            right[i] = if stack.is_empty() { n as i32 } else { *stack.last().unwrap() as i32 };
            stack.push(i);
        }
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = (pref[i] + strength[i] as i64) % MOD;
        }
        let mut pref_pref = vec![0i64; n + 2];
        for i in 0..=n {
            pref_pref[i + 1] = (pref_pref[i] + pref[i]) % MOD;
        }
        let mut ans = 0i64;
        for i in 0..n {
            let l = left[i] + 1;
            let r = right[i] - 1;
            let left_sum = (pref_pref[i + 1] - pref_pref[l as usize] + MOD) % MOD;
            let right_sum = (pref_pref[r as usize + 2] - pref_pref[i + 1] + MOD) % MOD;
            let left_cnt = i as i64 - l as i64 + 1;
            let right_cnt = r as i64 - i as i64 + 1;
            let contrib = (right_cnt * left_sum % MOD - left_cnt * right_sum % MOD + MOD) % MOD;
            ans = (ans + contrib * strength[i] as i64 % MOD) % MOD;
        }
        ans as i32
    }
}
