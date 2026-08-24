<?php
// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @param String $fill
     * @return String[]
     */
    function divideString($s, $k, $fill) {
        $ans = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i += $k) {
            if ($i + $k <= $n) $ans[] = substr($s, $i, $k);
            else {
                $chunk = substr($s, $i);
                while (strlen($chunk) < $k) $chunk .= $fill;
                $ans[] = $chunk;
            }
        }
        return $ans;
    }
}
