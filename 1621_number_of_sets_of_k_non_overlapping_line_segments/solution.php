<?php
// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution {
    private function comb($n, $k) {
        if ($k < 0 || $k > $n) {
            return 0;
        }
        $k = min($k, $n - $k);
        $res = 1;
        for ($i = 1; $i <= $k; $i++) {
            $res = intdiv($res * ($n - $k + $i), $i);
        }
        return $res;
    }

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numberOfSets($n, $k) {
        return $this->comb($n + $k - 1, 2 * $k) % 1000000007;
    }
}
