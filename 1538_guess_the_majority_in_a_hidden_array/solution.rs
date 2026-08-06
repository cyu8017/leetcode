// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

struct ArrayReader {
    nums: Vec<i32>,
}

impl ArrayReader {
    fn query(&self, a: i32, b: i32, c: i32, d: i32) -> i32 {
        let ones = self.nums[a as usize]
            + self.nums[b as usize]
            + self.nums[c as usize]
            + self.nums[d as usize];
        match ones {
            0 | 4 => 4,
            1 | 3 => 2,
            _ => 0,
        }
    }

    fn length(&self) -> i32 {
        self.nums.len() as i32
    }
}

impl Solution {
    pub fn guess_majority(nums: Vec<i32>) -> i32 {
        let reader = ArrayReader { nums };
        let n = reader.length();
        let first_four = reader.query(0, 1, 2, 3);
        let shifted = reader.query(1, 2, 3, 4);
        let mut same = 1;
        let mut different = 0;
        let mut different_index = -1;
        let mut later_different = -1;
        let four_same = first_four == shifted;
        if four_same {
            same += 1;
        } else {
            different += 1;
            different_index = 4;
        }
        let checks = [[0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4]];
        for (index, args) in checks.iter().enumerate() {
            if reader.query(args[0], args[1], args[2], args[3]) == shifted {
                same += 1;
            } else {
                different += 1;
                different_index = (index + 1) as i32;
            }
        }
        for i in 5..n {
            let i_same_as_four = reader.query(1, 2, 3, i) == shifted;
            if i_same_as_four == four_same {
                same += 1;
            } else {
                different += 1;
                different_index = i;
                if later_different == -1 {
                    later_different = i;
                }
            }
        }
        if same == different {
            return -1;
        }
        if same > different {
            return 0;
        }
        if later_different != -1 {
            later_different
        } else {
            different_index
        }
    }
}
