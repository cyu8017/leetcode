<?php
// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

class Solution {
    function minEnd($n, $x) {
        $n--;
        $ans = $x;
        for ($i = 0; $i < 31; $i++) {
            if ((($x >> $i) & 1) === 0) {
                $ans |= ($n & 1) << $i;
                $n >>= 1;
            }
        }
        $ans |= $n << 31;
        return $ans;
    }
}
