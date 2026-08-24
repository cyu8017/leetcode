<?php
// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

class Solution {
    function minOrAfterOperations($nums, $k) {
        $ans = 0;
        $rans = 0;
        for ($i = 29; $i >= 0; $i--) {
            $test = $ans + (1 << $i);
            $cnt = 0;
            $val = 0;
            foreach ($nums as $num) {
                if ($val === 0) $val = $test & $num;
                else $val &= $test & $num;
                if ($val !== 0) $cnt++;
            }
            if ($cnt > $k) $rans += (1 << $i);
            else $ans += (1 << $i);
        }
        return $rans;
    }
}
