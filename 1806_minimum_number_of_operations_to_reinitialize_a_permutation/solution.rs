// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

impl Solution {
    pub fn reinitialize_permutation(n: i32) -> i32 {
        let n = n as usize;
        let mut perm: Vec<usize> = (0..n).collect();
        let target = perm.clone();
        let mut operations = 0;

        loop {
            let mut new_perm = vec![0; n];
            for i in 0..n {
                if i % 2 == 0 {
                    new_perm[i] = perm[i / 2];
                } else {
                    new_perm[i] = perm[n / 2 + (i - 1) / 2];
                }
            }
            perm = new_perm;
            operations += 1;
            if perm == target {
                return operations;
            }
        }
    }
}
