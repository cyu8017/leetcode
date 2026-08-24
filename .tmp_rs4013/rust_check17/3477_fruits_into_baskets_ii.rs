struct Solution;
// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        let mut used = vec![false; baskets.len()];
        let mut unplaced = 0;
        for f in fruits {
            let mut placed = false;
            for j in 0..baskets.len() {
                if !used[j] && baskets[j] >= f {
                    used[j] = true;
                    placed = true;
                    break;
                }
            }
            if !placed {
                unplaced += 1;
            }
        }
        unplaced
    }
}

fn main() {}
