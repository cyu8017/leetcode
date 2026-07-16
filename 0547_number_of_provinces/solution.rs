// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut parent: Vec<usize> = (0..n).collect();

        fn find(parent: &mut Vec<usize>, node: usize) -> usize {
            if parent[node] != node {
                let root = find(parent, parent[node]);
                parent[node] = root;
            }
            parent[node]
        }

        for row in 0..n {
            for col in (row + 1)..n {
                if is_connected[row][col] == 1 {
                    let root_left = find(&mut parent, row);
                    let root_right = find(&mut parent, col);
                    if root_left != root_right {
                        parent[root_right] = root_left;
                    }
                }
            }
        }

        (0..n).filter(|&index| find(&mut parent, index) == index).count() as i32
    }
}
