<?php
// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

class Solution {
    /**
     * @param String $rings
     * @return Integer
     */
    function countPoints($rings) {
        $mask = array_fill(0, 10, 0);
        $len = strlen($rings);
        for ($i = 0; $i < $len; $i += 2) {
            $c = $rings[$i];
            $r = ord($rings[$i + 1]) - 48;
            $bit = $c === 'R' ? 1 : ($c === 'G' ? 2 : 4);
            $mask[$r] |= $bit;
        }
        $ans = 0;
        foreach ($mask as $m) if ($m === 7) $ans++;
        return $ans;
    }
}
