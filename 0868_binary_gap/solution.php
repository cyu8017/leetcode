<?php
// LeetCode 0868 - Binary Gap
// https://leetcode.com/problems/binary-gap/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function binaryGap($n) {
        $last = -1;
        $ans = 0;
        $bit = 0;
        while ($n !== 0) {
            if (($n & 1) === 1) {
                if ($last !== -1) $ans = max($ans, $bit - $last);
                $last = $bit;
            }
            $n >>= 1;
            $bit++;
        }
        return $ans;
    }
}
