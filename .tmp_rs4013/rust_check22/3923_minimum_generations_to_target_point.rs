struct Solution;
// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

use std::collections::BTreeMap;

impl Solution {
    pub fn min_generations(points: Vec<Vec<i32>>, target: Vec<i32>) -> i32 {
        type Point = [i32; 3];
        let target_point: Point = [target[0], target[1], target[2]];
        let mut generation: BTreeMap<Point, i32> = BTreeMap::new();
        let mut all: Vec<Point> = Vec::new();
        for values in points {
            let p: Point = [values[0], values[1], values[2]];
            generation.insert(p, 0);
            all.push(p);
        }
        if generation.contains_key(&target_point) {
            return generation[&target_point];
        }
        let mut current = 1;
        loop {
            let limit = all.len();
            let mut added = Vec::new();
            for i in 0..limit {
                for j in (i + 1)..limit {
                    if all[i] == all[j] {
                        continue;
                    }
                    let p: Point = [
                        (all[i][0] + all[j][0]) / 2,
                        (all[i][1] + all[j][1]) / 2,
                        (all[i][2] + all[j][2]) / 2,
                    ];
                    if !generation.contains_key(&p) {
                        generation.insert(p, current);
                        added.push(p);
                    }
                }
            }
            if generation.contains_key(&target_point) {
                return generation[&target_point];
            }
            if added.is_empty() {
                return -1;
            }
            all.extend(added);
            current += 1;
        }
    }
}

fn main() {}
