<?php
// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

class Solution {
    function smallestUniqueSubarray($nums) {
        $n = count($nums);
        $sa = range(0, $n - 1);
        $rank = $nums;
        for ($width = 1; $width < $n; $width <<= 1) {
            $w = $width;
            $r = $rank;
            usort($sa, function ($a, $b) use ($r, $w, $n) {
                if ($r[$a] != $r[$b]) return $r[$a] <=> $r[$b];
                $ra = $a + $w < $n ? $r[$a + $w] : -1;
                $rb = $b + $w < $n ? $r[$b + $w] : -1;
                return $ra <=> $rb;
            });
            $next = array_fill(0, $n, 0);
            for ($i = 1; $i < $n; $i++) {
                $a = $sa[$i - 1];
                $b = $sa[$i];
                $different = $rank[$a] != $rank[$b];
                $ra = $a + $width < $n ? $rank[$a + $width] : -1;
                $rb = $b + $width < $n ? $rank[$b + $width] : -1;
                $next[$b] = ($different || $ra != $rb) ? $next[$a] + 1 : $next[$a];
            }
            $rank = $next;
            if ($rank[$sa[$n - 1]] == $n - 1) break;
        }
        $pos = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $pos[$sa[$i]] = $i;
        $lcp = $n > 1 ? array_fill(0, $n - 1, 0) : [];
        $height = 0;
        for ($i = 0; $i < $n; $i++) {
            $p = $pos[$i];
            if ($p == $n - 1) {
                $height = 0;
                continue;
            }
            $j = $sa[$p + 1];
            while ($i + $height < $n && $j + $height < $n && $nums[$i + $height] == $nums[$j + $height]) $height++;
            $lcp[$p] = $height;
            if ($height > 0) $height--;
        }
        $ans = $n;
        for ($p = 0; $p < $n; $p++) {
            $start = $sa[$p];
            $need = 1;
            if ($p > 0 && $lcp[$p - 1] + 1 > $need) $need = $lcp[$p - 1] + 1;
            if ($p + 1 < $n && $lcp[$p] + 1 > $need) $need = $lcp[$p] + 1;
            if ($need <= $n - $start && $need < $ans) $ans = $need;
        }
        return $ans;
    }
}
