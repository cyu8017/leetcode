// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        fn lis(arr: &[i32]) -> i32 {
            let mut g = Vec::new();
            for &x in arr {
                match g.binary_search(&x) {
                    Ok(_) => {}
                    Err(i) => {
                        if i == g.len() {
                            g.push(x);
                        } else {
                            g[i] = x;
                        }
                    }
                }
            }
            g.len() as i32
        }
        let mx = *nums.iter().max().unwrap_or(&0);
        let m = if mx == 0 { 0 } else { 32 - mx.leading_zeros() };
        let mut ans = 0;
        for i in 0..m {
            let arr: Vec<i32> = nums.iter().copied().filter(|&x| ((x >> i) & 1) == 1).collect();
            ans = ans.max(lis(&arr));
        }
        ans
    }
}
