// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

pub struct NumArray {
    nums: Vec<i32>,
    tree: Vec<i32>,
    size: i32,
}

impl NumArray {
    pub fn new(nums: Vec<i32>) -> Self {
        let size = nums.len() as i32;
        let mut obj = Self {
            nums,
            tree: vec![0; size as usize + 1],
            size,
        };
        for index in 0..obj.size {
            obj.add(index + 1, obj.nums[index as usize]);
        }
        obj
    }

    fn add(&mut self, mut index: i32, delta: i32) {
        while index <= self.size {
            self.tree[index as usize] += delta;
            index += index & -index;
        }
    }

    fn prefix(&self, mut index: i32) -> i32 {
        let mut total = 0;
        while index > 0 {
            total += self.tree[index as usize];
            index -= index & -index;
        }
        total
    }

    pub fn update(&mut self, index: i32, val: i32) {
        let delta = val - self.nums[index as usize];
        self.nums[index as usize] = val;
        self.add(index + 1, delta);
    }

    pub fn sum_range(&self, left: i32, right: i32) -> i32 {
        self.prefix(right + 1) - self.prefix(left)
    }
}
