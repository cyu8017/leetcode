// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let n = a.len();
        let mut seen_a = vec![0u8; n + 1];
        let mut seen_b = vec![0u8; n + 1];
        let mut ans = vec![0; n];
        let mut common = 0;
        for i in 0..n {
            if seen_b[a[i] as usize] != 0 {
                common += 1;
            }
            seen_a[a[i] as usize] = 1;
            if seen_a[b[i] as usize] != 0 {
                common += 1;
            }
            seen_b[b[i] as usize] = 1;
            ans[i] = common;
        }
        ans
    }
}
