<?php
// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

class Solution {
    function maxSubstringLength($s, $k) {
        $n = strlen($s);
        $first = array_fill(0, 26, $n);
        $last = array_fill(0, 26, -1);
        for ($i = 0; $i < $n; $i++) {
            $ci = ord($s[$i]) - 97;
            if ($first[$ci] === $n) $first[$ci] = $i;
            $last[$ci] = $i;
        }
        $segs = [];
        for ($c = 0; $c < 26; $c++) {
            if ($last[$c] === -1) continue;
            $l = $first[$c];
            $r = $last[$c];
            for ($i = $l; $i <= $r; $i++) {
                $ci = ord($s[$i]) - 97;
                if ($first[$ci] < $l) {
                    $l = $first[$ci];
                    $i = $l - 1;
                    continue;
                }
                if ($last[$ci] > $r) $r = $last[$ci];
            }
            if (!($l === 0 && $r === $n - 1)) $segs[] = [$l, $r];
        }
        $uniq = [];
        $arr = [];
        foreach ($segs as $sg) {
            $ks = $sg[0] . "," . $sg[1];
            if (!isset($uniq[$ks])) {
                $uniq[$ks] = true;
                $arr[] = $sg;
            }
        }
        usort($arr, function($a, $b) { return $a[1] <=> $b[1]; });
        $cnt = 0;
        $end = -1;
        foreach ($arr as $sg) {
            if ($sg[0] > $end) {
                $cnt++;
                $end = $sg[1];
            }
        }
        return $cnt >= $k;
    }
}
