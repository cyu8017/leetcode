<?php
// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

class Solution {
    function maxSubarrays($n, $conflictingPairs) {
        $m = count($conflictingPairs);
        $best = 0;
        for ($skip = 0; $skip < $m; $skip++) {
            $rightLimit = array_fill(0, $n + 2, $n + 1);
            for ($i = 0; $i < $m; $i++) {
                if ($i === $skip) continue;
                $a = $conflictingPairs[$i][0];
                $b = $conflictingPairs[$i][1];
                if ($a > $b) { $t = $a; $a = $b; $b = $t; }
                if ($b < $rightLimit[$a]) $rightLimit[$a] = $b;
            }
            $minRight = $n + 1;
            $cnt = 0;
            for ($l = $n; $l >= 1; $l--) {
                if ($rightLimit[$l] < $minRight) $minRight = $rightLimit[$l];
                $cnt += $minRight - $l;
            }
            if ($cnt > $best) $best = $cnt;
        }
        return $best;
    }
}
