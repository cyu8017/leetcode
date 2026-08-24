<?php
// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        $write = 0;
        for ($read = 0; $read < count($nums); $read++) {
            if ($nums[$read] !== $val) {
                $nums[$write] = $nums[$read];
                $write++;
            }
        }
        return $write;
    }
}
