// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

class Solution {
    func createInfiniteObject() -> (String) -> String {
        { _ in "Hello World" }
    }
}
