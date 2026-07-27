<?php
// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function specialArray($nums) {
        $n = count($nums);
        for ($x = 0; $x <= $n; $x++) {
            $cnt = 0;
            foreach ($nums as $v) {
                if ($v >= $x) {
                    $cnt++;
                }
            }
            if ($cnt === $x) {
                return $x;
            }
        }
        return -1;
    }
}
