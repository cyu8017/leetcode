// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

pub struct Expect {
    val: i32,
}

impl Expect {
    pub fn new(val: i32) -> Self {
        Self { val }
    }

    pub fn to_be(&self, other: i32) -> Result<bool, &'static str> {
        if self.val == other {
            Ok(true)
        } else {
            Err("Not Equal")
        }
    }

    pub fn not_to_be(&self, other: i32) -> Result<bool, &'static str> {
        if self.val != other {
            Ok(true)
        } else {
            Err("Equal")
        }
    }
}

impl Solution {
    pub fn expect(val: i32) -> Expect {
        Expect::new(val)
    }
}
