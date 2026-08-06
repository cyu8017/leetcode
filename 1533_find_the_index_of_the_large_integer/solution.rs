// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

struct ArrayReader {
    arr: Vec<i32>,
}

impl ArrayReader {
    fn compare_sub(&self, l: i32, r: i32, x: i32, y: i32) -> i32 {
        let a: i32 = self.arr[l as usize..=r as usize].iter().sum();
        let b: i32 = self.arr[x as usize..=y as usize].iter().sum();
        a.cmp(&b) as i32
    }

    fn length(&self) -> i32 {
        self.arr.len() as i32
    }
}

impl Solution {
    pub fn get_index(arr: Vec<i32>) -> i32 {
        let reader = ArrayReader { arr };
        let mut left = 0;
        let mut right = reader.length() - 1;
        while left < right {
            let length = right - left + 1;
            let half = length / 2;
            let result = reader.compare_sub(left, left + half - 1, right - half + 1, right);
            if result == 0 {
                return left + half;
            }
            if result > 0 {
                right = left + half - 1;
            } else {
                left = right - half + 1;
            }
        }
        left
    }
}
