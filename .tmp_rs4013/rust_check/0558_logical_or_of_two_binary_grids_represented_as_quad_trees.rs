struct Solution;
// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

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
    pub fn intersect(quad_tree1: Option<Box<Node>>, quad_tree2: Option<Box<Node>>) -> Option<Box<Node>> {
        let a = quad_tree1?;
        let b = quad_tree2?;
        if a.is_leaf {
            return if a.val { Some(a) } else { Some(b) };
        }
        if b.is_leaf {
            return if b.val { Some(b) } else { Some(a) };
        }
        let top_left = Self::intersect(a.top_left, b.top_left);
        let top_right = Self::intersect(a.top_right, b.top_right);
        let bottom_left = Self::intersect(a.bottom_left, b.bottom_left);
        let bottom_right = Self::intersect(a.bottom_right, b.bottom_right);
        if let (Some(tl), Some(tr), Some(bl), Some(br)) = (
            top_left.as_ref(),
            top_right.as_ref(),
            bottom_left.as_ref(),
            bottom_right.as_ref(),
        ) {
            if tl.is_leaf
                && tr.is_leaf
                && bl.is_leaf
                && br.is_leaf
                && tl.val == tr.val
                && tr.val == bl.val
                && bl.val == br.val
            {
                return Some(Box::new(Node {
                    val: tl.val,
                    is_leaf: true,
                    top_left: None,
                    top_right: None,
                    bottom_left: None,
                    bottom_right: None,
                }));
            }
        }
        Some(Box::new(Node {
            val: false,
            is_leaf: false,
            top_left,
            top_right,
            bottom_left,
            bottom_right,
        }))
    }
}

fn main() {}
