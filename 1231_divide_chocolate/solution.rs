// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

impl Solution {
    pub fn maximize_sweetness(sweetness: Vec<i32>, k: i32) -> i32 {
        let total: i32 = sweetness.iter().sum();
        let mut lo = 1;
        let mut hi = total / (k + 1);
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let mut pieces = 0;
            let mut current = 0;
            for &value in &sweetness {
                current += value;
                if current >= mid {
                    pieces += 1;
                    current = 0;
                }
            }
            if pieces >= k + 1 {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        hi
    }
}
