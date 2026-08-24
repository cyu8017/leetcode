// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

impl Solution {
    pub fn create_infinite_object() -> impl Fn(String) -> String {
        |_| "Hello World".to_string()
    }
}
