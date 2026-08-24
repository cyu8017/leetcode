// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let mx = (*nums.iter().max().unwrap() as usize) << 1;
        let mut st = vec![0u8; mx];
        for &a in &nums {
            for &b in &nums {
                st[(a ^ b) as usize] = 1;
            }
        }
        let mut s = vec![0i32; mx];
        for ab in 0..mx {
            if st[ab] != 0 {
                for &c in &nums {
                    s[ab ^ c as usize] = 1;
                }
            }
        }
        s.iter().sum()
    }
}
