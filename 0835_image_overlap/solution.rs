// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

use std::collections::HashMap;

impl Solution {
    pub fn largest_overlap(img1: Vec<Vec<i32>>, img2: Vec<Vec<i32>>) -> i32 {
        let n = img1.len() as i32;
        let mut ones1 = Vec::new();
        let mut ones2 = Vec::new();
        for i in 0..img1.len() {
            for j in 0..img1[0].len() {
                if img1[i][j] != 0 {
                    ones1.push((i as i32, j as i32));
                }
                if img2[i][j] != 0 {
                    ones2.push((i as i32, j as i32));
                }
            }
        }
        if ones1.is_empty() || ones2.is_empty() {
            return 0;
        }
        let mut shifts = HashMap::new();
        let mut best = 0;
        for &(x1, y1) in &ones1 {
            for &(x2, y2) in &ones2 {
                let key = ((x1 - x2 + n) as i64) << 16 | (y1 - y2 + n) as i64;
                let entry = shifts.entry(key).or_insert(0);
                *entry += 1;
                best = best.max(*entry);
            }
        }
        best
    }
}
