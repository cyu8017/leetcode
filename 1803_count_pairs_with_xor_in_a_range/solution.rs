// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

struct TrieNode {
    count: i32,
    children: [Option<Box<TrieNode>>; 2],
}

impl TrieNode {
    fn new() -> Self {
        Self {
            count: 0,
            children: [None, None],
        }
    }
}

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, low: i32, high: i32) -> i32 {
        Self::count_smaller_than(&nums, high + 1) - Self::count_smaller_than(&nums, low)
    }

    fn count_smaller_than(nums: &[i32], limit: i32) -> i32 {
        if limit <= 0 {
            return 0;
        }
        let mut root = TrieNode::new();
        let mut total = 0;
        const MAX_BIT: i32 = 15;
        for &num in nums {
            total += Self::query(&root, num, limit, MAX_BIT);
            Self::insert(&mut root, num, MAX_BIT);
        }
        total
    }

    fn insert(root: &mut TrieNode, num: i32, bit: i32) {
        let mut node = root;
        for i in (0..=bit).rev() {
            let b = ((num >> i) & 1) as usize;
            if node.children[b].is_none() {
                node.children[b] = Some(Box::new(TrieNode::new()));
            }
            node = node.children[b].as_mut().unwrap();
            node.count += 1;
        }
    }

    fn query(root: &TrieNode, num: i32, limit: i32, bit: i32) -> i32 {
        if bit < 0 {
            return 0;
        }
        let num_bit = ((num >> bit) & 1) as usize;
        let limit_bit = (limit >> bit) & 1;
        if limit_bit == 1 {
            let mut result = root.children[num_bit]
                .as_ref()
                .map(|c| c.count)
                .unwrap_or(0);
            if let Some(child) = root.children[1 - num_bit].as_ref() {
                result += Self::query(child, num, limit, bit - 1);
            }
            result
        } else if let Some(child) = root.children[num_bit].as_ref() {
            Self::query(child, num, limit, bit - 1)
        } else {
            0
        }
    }
}
