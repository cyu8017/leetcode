// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn num_squares(n: i32) -> i32 {
        let mut squares = Vec::new();
        let mut value = 1;
        while value * value <= n {
            squares.push(value * value);
            value += 1;
        }

        let mut queue = VecDeque::from([(n, 0)]);
        let mut visited = HashSet::from([n]);

        while let Some((remain, steps)) = queue.pop_front() {
            if remain == 0 {
                return steps;
            }
            for square in squares {
                let next = remain - square;
                if next < 0 {
                    break;
                }
                if visited.insert(next) {
                    queue.push_back((next, steps + 1));
                }
            }
        }
        0
    }
}
