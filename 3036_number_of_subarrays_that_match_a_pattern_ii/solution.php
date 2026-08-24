<?php
// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

class Solution {
    function countMatchingSubarrays($nums, $pattern) {
        $N = count($pattern);
        $ps = array_fill(0, $N + 1, 0);
        $ps[0] = -1;
        $ps[1] = 0;
        for ($i = 2, $p = 0; $i <= $N; $i++) {
            $x = $pattern[$i - 1];
            while ($p >= 0 && $pattern[$p] !== $x) $p = $ps[$p];
            $p++;
            $ps[$i] = $p;
        }
        $res = 0;
        $M = count($nums);
        for ($i = 1, $p = 0; $i < $M; $i++) {
            $t = $nums[$i] - $nums[$i - 1];
            if ($t > 0) $t = 1;
            else if ($t < 0) $t = -1;
            while ($p >= 0 && $pattern[$p] !== $t) $p = $ps[$p];
            if (++$p === $N) {
                $res++;
                $p = $ps[$p];
            }
        }
        return $res;
    }
}
