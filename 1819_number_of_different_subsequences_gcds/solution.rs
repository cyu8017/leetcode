// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

impl Solution {
    pub fn count_different_subsequence_gcds(nums: Vec<i32>) -> i32 {
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut present = vec![false; max_val + 1];
        for num in nums {
            present[num as usize] = true;
        }

        let mut ans = 0;
        for g in 1..=max_val {
            let mut has = false;
            let mut gcd_val = 0usize;
            let mut multiple = g;
            while multiple <= max_val {
                if present[multiple] {
                    has = true;
                    gcd_val = Self::gcd(gcd_val, multiple / g);
                    if gcd_val == 1 {
                        break;
                    }
                }
                multiple += g;
            }
            if has && gcd_val == 1 {
                ans += 1;
            }
        }
        ans
    }

    fn gcd(mut a: usize, mut b: usize) -> usize {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }
}
