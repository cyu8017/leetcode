<?php
// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countPairs($nums, $k) {
        $freq = [];
        $ans = 0;
        foreach ($nums as $x) {
            $g1 = $this->gcd($x, $k);
            foreach ($freq as $g2 => $cnt) {
                if (($g1 * $g2) % $k === 0) $ans += $cnt;
            }
            $freq[$g1] = ($freq[$g1] ?? 0) + 1;
        }
        return $ans;
    }
}
