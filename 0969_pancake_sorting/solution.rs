// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

impl Solution {
    pub fn pancake_sort(arr: Vec<i32>) -> Vec<i32> {
        let mut a = arr;
        let mut ans = Vec::new();
        for size in (2..=a.len()).rev() {
            let i = a.iter().position(|&x| x == size as i32).unwrap();
            if i == size - 1 {
                continue;
            }
            if i > 0 {
                ans.push(i as i32 + 1);
                a[..=i].reverse();
            }
            ans.push(size as i32);
            a[..size].reverse();
        }
        ans
    }
}
