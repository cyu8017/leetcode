// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

struct SegNode {
    left: Option<Box<SegNode>>,
    right: Option<Box<SegNode>>,
    covered: bool,
}

impl SegNode {
    fn new() -> Self {
        Self {
            left: None,
            right: None,
            covered: false,
        }
    }
}

pub struct CountIntervals {
    root: Option<Box<SegNode>>,
    cnt: i32,
}

impl CountIntervals {
    pub fn new() -> Self {
        Self { root: None, cnt: 0 }
    }

    fn add_seg(l_bound: i32, r_bound: i32, l: i32, r: i32, node: &mut Option<Box<SegNode>>) -> i32 {
        if node.is_none() {
            *node = Some(Box::new(SegNode::new()));
        }
        let n = node.as_mut().unwrap();
        if n.covered {
            return 0;
        }
        if l <= l_bound && r_bound <= r {
            n.covered = true;
            n.left = None;
            n.right = None;
            return r_bound - l_bound + 1;
        }
        let mid = l_bound + (r_bound - l_bound) / 2;
        let mut added = 0;
        if l <= mid {
            added += Self::add_seg(l_bound, mid, l, r, &mut n.left);
        }
        if r > mid {
            added += Self::add_seg(mid + 1, r_bound, l, r, &mut n.right);
        }
        if n.left.as_ref().map(|x| x.covered).unwrap_or(false)
            && n.right.as_ref().map(|x| x.covered).unwrap_or(false)
        {
            n.covered = true;
            n.left = None;
            n.right = None;
        }
        added
    }

    pub fn add(&mut self, left: i32, right: i32) {
        self.cnt += Self::add_seg(1, 1_000_000_000, left, right, &mut self.root);
    }

    pub fn count(&self) -> i32 {
        self.cnt
    }
}
