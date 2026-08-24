<?php
// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

class Solution {
    function minBitwiseArray($nums) {
        $ans = array_fill(0, count($nums), -1);
        for ($i = 0; $i < count($nums); $i++) {
            $n = $nums[$i];
            if ($n === 2) continue;
            for ($b = 0; $b < 31; $b++) {
                if ((($n >> $b) & 1) === 0) continue;
                $x = $n ^ (1 << $b);
                if (($x | ($x + 1)) === $n) { $ans[$i] = $x; break; }
            }
        }
        return $ans;
    }
}
