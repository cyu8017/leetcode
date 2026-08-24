struct Solution;
// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        let n = baskets.len();
        let mut size = 1;
        while size < n {
            size <<= 1;
        }
        let mut tree = vec![0; size * 2];
        for i in 0..n {
            tree[size + i] = baskets[i];
        }
        for i in (1..size).rev() {
            tree[i] = tree[i * 2].max(tree[i * 2 + 1]);
        }
        fn find(tree: &[i32], node: usize, nl: usize, nr: usize, need: i32) -> i32 {
            if tree[node] < need {
                return -1;
            }
            if nl == nr {
                return nl as i32;
            }
            let mid = (nl + nr) / 2;
            let left = find(tree, node * 2, nl, mid, need);
            if left != -1 {
                return left;
            }
            find(tree, node * 2 + 1, mid + 1, nr, need)
        }
        let update = |tree: &mut [i32], idx: usize, size: usize| {
            let mut p = size + idx;
            tree[p] = -1;
            p >>= 1;
            while p > 0 {
                tree[p] = tree[p * 2].max(tree[p * 2 + 1]);
                p >>= 1;
            }
        };
        let mut unplaced = 0;
        for f in fruits {
            let idx = find(&tree, 1, 0, size - 1, f);
            if idx == -1 || idx >= n as i32 {
                unplaced += 1;
            } else {
                update(&mut tree, idx as usize, size);
            }
        }
        unplaced
    }
}

fn main() {}
