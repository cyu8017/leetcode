<?php
// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function nextGreaterElement($nums1, $nums2) {
        return $this->next_greater_element($nums1, $nums2);
    }

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function next_greater_element($nums1, $nums2) {
        $nextGreater = [];
        $stack = [];
        foreach ($nums2 as $num) {
            while ($stack !== [] && $stack[count($stack) - 1] < $num) {
                $nextGreater[array_pop($stack)] = $num;
            }
            $stack[] = $num;
        }
        $result = [];
        foreach ($nums1 as $num) {
            $result[] = $nextGreater[$num] ?? -1;
        }
        return $result;
    }
}
