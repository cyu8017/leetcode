// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

impl Solution {
    pub fn get_results(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut a = nums;
        let mut ans = Vec::new();
        for q in queries {
            let typ = q[0];
            if typ == 1 {
                let mut l = q[1] as usize;
                let mut r = q[2] as usize;
                while l < r {
                    a.swap(l, r);
                    l += 1;
                    r -= 1;
                }
            } else if typ == 2 {
                let l = q[1] as usize;
                let r = q[2] as usize;
                let mut x = 0;
                for i in l..=r {
                    x ^= a[i];
                }
                ans.push(x);
            } else {
                a[q[1] as usize] = q[2];
            }
        }
        ans
    }
}
