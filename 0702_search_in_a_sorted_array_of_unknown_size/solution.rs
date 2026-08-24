// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

struct ArrayReader {
    secret: Vec<i32>,
}

impl ArrayReader {
    fn new(secret: Vec<i32>) -> Self {
        Self { secret }
    }

    fn get(&self, index: i32) -> i32 {
        if index < 0 || index as usize >= self.secret.len() {
            i32::MAX
        } else {
            self.secret[index as usize]
        }
    }
}

impl Solution {
    pub fn search(secret: Vec<i32>, target: i32) -> i32 {
        Self::search_reader(&ArrayReader::new(secret), target)
    }

    fn search_reader(reader: &ArrayReader, target: i32) -> i32 {
        let mut right = 1;
        while reader.get(right) < target {
            right <<= 1;
        }
        let mut left = right >> 1;
        while left <= right {
            let mid = left + (right - left) / 2;
            let value = reader.get(mid);
            if value == target {
                return mid;
            }
            if value > target {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        -1
    }
}
