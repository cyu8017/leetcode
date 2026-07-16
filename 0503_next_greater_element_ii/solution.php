<?php
// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function nextGreaterElements($nums) {
        return $this->next_greater_elements($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function next_greater_elements($nums) {
        $length = count($nums);
        $result = array_fill(0, $length, -1);
        $stack = [];
        for ($index = 0; $index < $length * 2; $index++) {
            while ($stack !== [] && $nums[$stack[count($stack) - 1]] < $nums[$index % $length]) {
                $result[array_pop($stack)] = $nums[$index % $length];
            }
            if ($index < $length) {
                $stack[] = $index;
            }
        }
        return $result;
    }
}
