struct Solution;
// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

use std::collections::HashMap;

impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        fn solve(nums: &[i32], start_zero: bool) -> i32 {
            let n = nums.len();
            let mut arr = nums.to_vec();
            let mut pos: HashMap<i32, usize> = HashMap::new();
            for i in 0..n {
                pos.insert(arr[i], i);
            }
            let mut ops = 0;
            loop {
                let empty = pos[&0];
                let should = if start_zero {
                    empty as i32
                } else if empty == n - 1 {
                    0
                } else {
                    empty as i32 + 1
                };
                if arr[empty] == should {
                    let mut found = None;
                    for i in 0..n {
                        let want = if start_zero {
                            i as i32
                        } else if i == n - 1 {
                            0
                        } else {
                            i as i32 + 1
                        };
                        if arr[i] != want {
                            found = Some(i);
                            break;
                        }
                    }
                    if found.is_none() {
                        return ops;
                    }
                    let found = found.unwrap();
                    let v = arr[found];
                    arr.swap(empty, found);
                    pos.insert(0, found);
                    pos.insert(v, empty);
                    ops += 1;
                    continue;
                }
                let j = pos[&should];
                let v = arr[j];
                arr.swap(empty, j);
                pos.insert(0, j);
                pos.insert(v, empty);
                ops += 1;
            }
        }
        solve(&nums, true).min(solve(&nums, false))
    }
}

fn main() {}
