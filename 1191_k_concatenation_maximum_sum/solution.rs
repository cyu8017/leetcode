// LeetCode 1191 - K-Concatenation Maximum Sum
// https://leetcode.com/problems/k-concatenation-maximum-sum/

impl Solution {
    pub fn k_concatenation_max_sum(arr: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn kadane(nums: &[i32]) -> i64 {
            let mut best = 0i64;
            let mut cur = 0i64;
            for &x in nums {
                cur += x as i64;
                if cur < 0 {
                    cur = 0;
                }
                best = best.max(cur);
            }
            best
        }
        let one = kadane(&arr);
        if k == 1 {
            return (one % MOD) as i32;
        }
        let mut two_arr = arr.clone();
        two_arr.extend_from_slice(&arr);
        let two = kadane(&two_arr);
        let total: i64 = arr.iter().map(|&x| x as i64).sum();
        let mut ans = one.max(two);
        if total > 0 {
            ans = ans.max(two + total * (k as i64 - 2));
        }
        (ans % MOD) as i32
    }
}
