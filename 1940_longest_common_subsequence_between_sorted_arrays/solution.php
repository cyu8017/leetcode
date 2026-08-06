<?php

class Solution {
    /**
     * @param Integer[][] $arrays
     * @return Integer[]
     */
    function longestCommonSubsequence($arrays) {
        $cnt = [];
        foreach ($arrays as $arr) {
            foreach ($arr as $x) {
                $cnt[$x] = ($cnt[$x] ?? 0) + 1;
            }
        }
        $m = count($arrays);
        $ans = [];
        foreach ($arrays[0] as $x) {
            if (($cnt[$x] ?? 0) === $m) {
                $ans[] = $x;
            }
        }
        return $ans;
    }
}
