// LeetCode 0276 - Paint Fence
// https://leetcode.com/problems/paint-fence/

impl Solution {
    pub fn num_ways(n: i32, k: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return k;
        }
        if n == 2 {
            return k * k;
        }
        let mut prev2 = k;
        let mut prev1 = k * k;
        for _ in 3..=n {
            let next = (prev1 + prev2) * (k - 1);
            prev2 = prev1;
            prev1 = next;
        }
        prev1
    }
}
