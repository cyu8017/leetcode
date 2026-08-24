// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

impl Solution {
    pub fn sort_jumbled(mapping: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        let map_val = |mut x: i32| {
            if x == 0 {
                return mapping[0];
            }
            let mut digits = Vec::new();
            while x > 0 {
                digits.push(x % 10);
                x /= 10;
            }
            let mut res = 0;
            for d in digits.iter().rev() {
                res = res * 10 + mapping[*d as usize];
            }
            res
        };
        let mut arr: Vec<(i32, usize, i32)> = nums
            .iter()
            .enumerate()
            .map(|(i, &x)| (map_val(x), i, x))
            .collect();
        arr.sort_unstable();
        arr.into_iter().map(|(_, _, x)| x).collect()
    }
}
