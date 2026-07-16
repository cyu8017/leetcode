// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: bool,
    pub is_leaf: bool,
    pub top_left: Option<Box<Node>>,
    pub top_right: Option<Box<Node>>,
    pub bottom_left: Option<Box<Node>>,
    pub bottom_right: Option<Box<Node>>,
}

impl Solution {
    pub fn construct(grid: Vec<Vec<i32>>) -> Option<Box<Node>> {
        fn build(grid: &Vec<Vec<i32>>, row: usize, col: usize, size: usize) -> Box<Node> {
            if size == 1 {
                return Box::new(Node {
                    val: grid[row][col] == 1,
                    is_leaf: true,
                    top_left: None,
                    top_right: None,
                    bottom_left: None,
                    bottom_right: None,
                });
            }

            let half = size / 2;
            let top_left = build(grid, row, col, half);
            let top_right = build(grid, row, col + half, half);
            let bottom_left = build(grid, row + half, col, half);
            let bottom_right = build(grid, row + half, col + half, half);

            if top_left.is_leaf
                && top_right.is_leaf
                && bottom_left.is_leaf
                && bottom_right.is_leaf
                && top_left.val == top_right.val
                && top_left.val == bottom_left.val
                && top_left.val == bottom_right.val
            {
                return Box::new(Node {
                    val: top_left.val,
                    is_leaf: true,
                    top_left: None,
                    top_right: None,
                    bottom_left: None,
                    bottom_right: None,
                });
            }

            Box::new(Node {
                val: true,
                is_leaf: false,
                top_left: Some(top_left),
                top_right: Some(top_right),
                bottom_left: Some(bottom_left),
                bottom_right: Some(bottom_right),
            })
        }

        Some(build(&grid, 0, 0, grid.len()))
    }
}
