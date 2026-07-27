<?php
// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

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
     * @param Integer[] $destination
     * @param Integer $k
     * @return String
     */
    function kthSmallestPath($destination, $k) {
        $v = $destination[0];
        $h = $destination[1];
        $ans = "";
        while ($h + $v) {
            if ($h) {
                $count = $this->comb($h + $v - 1, $v);
                if ($k <= $count) {
                    $ans .= "H";
                    $h--;
                    continue;
                }
                $k -= $count;
            }
            $ans .= "V";
            $v--;
        }
        return $ans;
    }
}
