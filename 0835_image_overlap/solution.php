<?php
// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

class Solution {
    /**
     * @param Integer[][] $img1
     * @param Integer[][] $img2
     * @return Integer
     */
    function largestOverlap($img1, $img2) {
        $n = count($img1);
        $ones1 = [];
        $ones2 = [];
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($img1[$i][$j] === 1) $ones1[] = [$i, $j];
                if ($img2[$i][$j] === 1) $ones2[] = [$i, $j];
            }
        }
        if (!count($ones1) || !count($ones2)) return 0;
        $shifts = [];
        $best = 0;
        foreach ($ones1 as $a) {
            foreach ($ones2 as $b) {
                $key = (($a[0] - $b[0] + $n) << 16) | ($a[1] - $b[1] + $n);
                $v = ($shifts[$key] ?? 0) + 1;
                $shifts[$key] = $v;
                $best = max($best, $v);
            }
        }
        return $best;
    }
}
