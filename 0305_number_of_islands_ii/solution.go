// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

use std::collections::HashMap;

impl Solution {
    pub fn num_islands2(m: i32, n: i32, positions: Vec<Vec<i32>>) -> Vec<i32> {
        let mut parent: HashMap<i32, i32> = HashMap::new();
        let mut rank: HashMap<i32, i32> = HashMap::new();

        fn find(parent: &mut HashMap<i32, i32>, rank: &mut HashMap<i32, i32>, index: i32) -> i32 {
            parent.entry(index).or_insert(index);
            rank.entry(index).or_insert(0);
            if parent[&index] != index {
                let root = find(parent, rank, parent[&index]);
                parent.insert(index, root);
            }
            parent[&index]
        }

        fn unite(
            parent: &mut HashMap<i32, i32>,
            rank: &mut HashMap<i32, i32>,
            left: i32,
            right: i32,
        ) -> bool {
            let root_left = find(parent, rank, left);
            let root_right = find(parent, rank, right);
            if root_left == root_right {
                return false;
            }
            let (root_left, root_right) = if rank[&root_left] < rank[&root_right] {
                (root_right, root_left)
            } else {
                (root_left, root_right)
            };
            parent.insert(root_right, root_left);
            if rank[&root_left] == rank[&root_right] {
                rank.insert(root_left, rank[&root_left] + 1);
            }
            true
        }

        let mut result = Vec::new();
        let mut islands = 0;
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];

        for position in positions {
            let row = position[0];
            let col = position[1];
            let index = row * n + col;
            if parent.contains_key(&index) {
                result.push(islands);
                continue;
            }
            parent.insert(index, index);
            rank.insert(index, 0);
            islands += 1;
            for (dr, dc) in directions {
                let next_row = row + dr;
                let next_col = col + dc;
                if next_row >= 0 && next_row < m && next_col >= 0 && next_col < n {
                    let neighbor = next_row * n + next_col;
                    if parent.contains_key(&neighbor) && unite(&mut parent, &mut rank, index, neighbor) {
                        islands -= 1;
                    }
                }
            }
            result.push(islands);
        }

        result
    }
}
