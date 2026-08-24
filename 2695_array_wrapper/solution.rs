// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

pub struct ArrayWrapper {
    nums: Vec<i32>,
}

impl ArrayWrapper {
    pub fn new(nums: Vec<i32>) -> Self {
        Self { nums }
    }

    pub fn value_of(&self) -> i32 {
        self.nums.iter().sum()
    }

    pub fn to_string(&self) -> String {
        let mut s = String::from("[");
        for (i, x) in self.nums.iter().enumerate() {
            if i > 0 {
                s.push(',');
            }
            s.push_str(&x.to_string());
        }
        s.push(']');
        s
    }
}

impl Solution {
    pub fn array_wrapper_create(nums: Vec<i32>) -> ArrayWrapper {
        ArrayWrapper::new(nums)
    }
}
