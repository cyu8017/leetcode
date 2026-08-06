// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

use std::collections::HashMap;

impl Solution {
    pub fn max_students(seats: Vec<Vec<char>>) -> i32 {
        let cols = seats[0].len();
        let mut valid_rows = Vec::new();
        for row in &seats {
            let mut available = 0;
            for (c, &cell) in row.iter().enumerate() {
                if cell == '.' {
                    available |= 1 << c;
                }
            }
            let masks: Vec<i32> = (0..(1 << cols))
                .filter(|&mask| mask & !available == 0 && mask & (mask << 1) == 0)
                .collect();
            valid_rows.push(masks);
        }
        let mut dp: HashMap<i32, i32> = HashMap::new();
        dp.insert(0, 0);
        for masks in valid_rows {
            let mut nxt = HashMap::new();
            for mask in masks {
                for (&previous, &count) in &dp {
                    if mask & (previous << 1) == 0 && mask & (previous >> 1) == 0 {
                        let val = count + mask.count_ones() as i32;
                        nxt.entry(mask).and_modify(|e| *e = (*e).max(val)).or_insert(val);
                    }
                }
            }
            dp = nxt;
        }
        *dp.values().max().unwrap_or(&0)
    }
}
