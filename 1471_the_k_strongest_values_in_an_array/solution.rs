// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

impl Solution {
    pub fn get_strongest(mut arr: Vec<i32>, k: i32) -> Vec<i32> {
        arr.sort_unstable();
        let median = arr[(arr.len() - 1) / 2];
        arr.sort_by_key(|&x| std::cmp::Reverse(((x - median).abs(), x)));
        arr.into_iter().take(k as usize).collect()
    }
}
