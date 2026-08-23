// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

import java.util.function.Function;

// JS infinite method object stand-in
class Solution {
    public Function<String, String> createInfiniteObject() {
        return ignored -> "Hello World";
    }
}
