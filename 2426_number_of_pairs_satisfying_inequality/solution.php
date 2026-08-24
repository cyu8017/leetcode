<?php
// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution {
    function numberOfPairs($nums1, $nums2, $diff) {
        $n = count($nums1);
        $arr = array_fill(0, $n, 0);
        $tmp = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $arr[$i] = $nums1[$i] - $nums2[$i];
        $mergeCount = function ($l, $r) use (&$mergeCount, &$arr, &$tmp, $diff) {
            if ($r - $l <= 1) return 0;
            $m = ($l + $r) >> 1;
            $ans = $mergeCount($l, $m) + $mergeCount($m, $r);
            $j = $m;
            for ($i = $l; $i < $m; $i++) {
                while ($j < $r && $arr[$j] < $arr[$i] - $diff) $j++;
                $ans += $r - $j;
            }
            $p = $l;
            $q = $m;
            $i2 = $l;
            while ($p < $m && $q < $r) {
                if ($arr[$p] <= $arr[$q]) $tmp[$i2++] = $arr[$p++];
                else $tmp[$i2++] = $arr[$q++];
            }
            while ($p < $m) $tmp[$i2++] = $arr[$p++];
            while ($q < $r) $tmp[$i2++] = $arr[$q++];
            for ($t = $l; $t < $r; $t++) $arr[$t] = $tmp[$t];
            return $ans;
        };
        return $mergeCount(0, $n);
    }
}
