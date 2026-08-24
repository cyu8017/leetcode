<?php
// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function elementInNums($nums, $queries) {
        $n = count($nums);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++) {
            $t = $queries[$i][0];
            $idx = $queries[$i][1];
            $cycle = $t % (2 * $n);
            if ($cycle < $n) {
                $size = $n - $cycle;
                $offset = $cycle;
            } else {
                $size = $cycle - $n;
                $offset = 0;
            }
            $ans[$i] = $idx >= $size ? -1 : $nums[$offset + $idx];
        }
        return $ans;
    }
}
