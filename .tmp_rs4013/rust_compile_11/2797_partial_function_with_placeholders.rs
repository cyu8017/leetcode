struct Solution;
fn main() {}

// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

impl Solution {
    pub fn partial<F: Fn(Vec<i32>) -> i32 + 'static>(
        fn_: F,
        args: Vec<i32>,
    ) -> Box<dyn Fn(Vec<i32>) -> i32> {
        Box::new(move |rest: Vec<i32>| {
            let mut full = Vec::new();
            let mut ri = 0;
            for &a in &args {
                if a == i32::MIN {
                    if ri < rest.len() {
                        full.push(rest[ri]);
                        ri += 1;
                    }
                } else {
                    full.push(a);
                }
            }
            while ri < rest.len() {
                full.push(rest[ri]);
                ri += 1;
            }
            fn_(full)
        })
    }
}
