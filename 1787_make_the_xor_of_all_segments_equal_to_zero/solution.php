<?php
// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minChanges($nums, $k) {
        $freq = array_fill(0, $k, []);
        $size = array_fill(0, $k, 0);
        foreach ($nums as $i => $x) {
            $g = $i % $k;
            $freq[$g][$x] = ($freq[$g][$x] ?? 0) + 1;
            $size[$g]++;
        }
        $inf = 1000000000;
        $dp = array_fill(0, 256, $inf);
        $dp[0] = 0;
        for ($i = 0; $i < $k; $i++) {
            $ndp = array_fill(0, 256, $inf);
            for ($xv = 0; $xv < 256; $xv++) {
                $cost = $size[$i] - ($freq[$i][$xv] ?? 0);
                for ($xo = 0; $xo < 256; $xo++) {
                    if ($dp[$xo] === $inf) {
                        continue;
                    }
                    $key = $xo ^ $xv;
                    if ($dp[$xo] + $cost < $ndp[$key]) {
                        $ndp[$key] = $dp[$xo] + $cost;
                    }
                }
            }
            $dp = $ndp;
        }
        return $dp[0];
    }
}
