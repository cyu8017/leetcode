// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

fn rand7() -> i32 {
    panic!("rand7 must be provided by the test harness");
}

impl Solution {
    pub fn rand10(&self) -> i32 {
        loop {
            let num = (rand7() - 1) * 7 + rand7();
            if num <= 40 {
                return (num - 1) % 10 + 1;
            }
        }
    }
}
