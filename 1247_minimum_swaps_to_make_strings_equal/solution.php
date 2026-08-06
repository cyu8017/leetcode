<?php
// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function minimumSwap($s1, $s2) {
        $xy = $yx = 0;
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            if ($s1[$i] === 'x' && $s2[$i] === 'y') $xy++;
            if ($s1[$i] === 'y' && $s2[$i] === 'x') $yx++;
        }
        if (($xy + $yx) % 2) return -1;
        return intdiv($xy, 2) + intdiv($yx, 2) + 2 * ($xy % 2);
    }
}
