<?php
// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

class Solution {
    function numGoodSubarrays($nums, $k) {
        $ans = 0;
        $s = 0;
        $cnt = [];
        $cnt[0] = 1;
        foreach ($nums as $x) {
            $s = ($s + $x) % $k;
            $ans += isset($cnt[$s]) ? $cnt[$s] : 0;
            if (!isset($cnt[$s])) $cnt[$s] = 0;
            $cnt[$s]++;
        }
        $n = count($nums);
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $nums[$j] === $nums[$i]) $j++;
            $m = $j - $i;
            for ($h = 1; $h <= $m; $h++) {
                if (($nums[$i] * $h) % $k === 0) $ans -= ($m - $h);
            }
            $i = $j;
        }
        return $ans;
    }
}
