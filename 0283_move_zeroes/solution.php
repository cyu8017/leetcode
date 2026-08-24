<?php
// LeetCode 0283 - Move Zeroes
// https://leetcode.com/problems/move-zeroes/

class Solution {
    /**
     * @param Integer[] $nums
     * @return void
     */
    function moveZeroes(&$nums) {
        $insert = 0;
        foreach ($nums as $num) {
            if ($num !== 0) {
                $nums[$insert] = $num;
                $insert++;
            }
        }
        for ($index = $insert; $index < count($nums); $index++) {
            $nums[$index] = 0;
        }
    }
}
