// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function productExceptSelf($nums) {
        $length = count($nums);
        $result = array_fill(0, $length, 1);
        $prefix = 1;
        for ($index = 0; $index < $length; $index++) {
            $result[$index] = $prefix;
            $prefix *= $nums[$index];
        }
        $suffix = 1;
        for ($index = $length - 1; $index >= 0; $index--) {
            $result[$index] *= $suffix;
            $suffix *= $nums[$index];
        }
        return $result;
    }
}
