// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        fn sig(x: i32) -> String {
            let mut chars: Vec<char> = x.to_string().chars().collect();
            chars.sort_unstable();
            chars.into_iter().collect()
        }
        let target = sig(n);
        (0..31).any(|i| sig(1 << i) == target)
    }
}
