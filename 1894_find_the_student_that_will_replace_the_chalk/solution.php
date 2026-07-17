<?php
// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution {
    /**
     * @param Integer[] $chalk
     * @param Integer $k
     * @return Integer
     */
    function chalkReplacer($chalk, $k) {
        $k %= array_sum($chalk);
        foreach ($chalk as $index => $need) {
            if ($k < $need) {
                return $index;
            }
            $k -= $need;
        }
        return 0;
    }
}
