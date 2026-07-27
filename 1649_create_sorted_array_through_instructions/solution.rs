// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

impl Solution {
    pub fn create_sorted_array(instructions: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mx = *instructions.iter().max().unwrap_or(&0) as usize;
        let size = mx + 2;
        let mut bit = vec![0i32; size + 1];
        let query = |bit: &[i32], mut i: usize| -> i32 {
            let mut s = 0;
            while i > 0 {
                s += bit[i];
                i -= i & i.wrapping_neg();
            }
            s
        };
        let update = |bit: &mut [i32], mut j: usize, size: usize| {
            while j <= size {
                bit[j] += 1;
                j += j & j.wrapping_neg();
            }
        };
        let mut ans = 0;
        for (i, &x) in instructions.iter().enumerate() {
            let less = query(&bit, x as usize - 1);
            let greater = i as i32 - query(&bit, x as usize);
            ans = (ans + less.min(greater)) % MOD;
            update(&mut bit, x as usize, size);
        }
        ans
    }
}
