<?php
// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDifference($nums) {
        $n = intdiv(count($nums), 2);
        $total = array_sum($nums);
        $left = array_slice($nums, 0, $n);
        $right = array_slice($nums, $n);
        $sumsByCount = function ($arr) {
            $m = count($arr);
            $res = array_fill(0, $m + 1, []);
            $lim = 1 << $m;
            for ($mask = 0; $mask < $lim; $mask++) {
                $sum = 0;
                $c = 0;
                for ($i = 0; $i < $m; $i++) if (($mask & (1 << $i)) !== 0) { $sum += $arr[$i]; $c++; }
                $res[$c][] = $sum;
            }
            foreach ($res as &$v) sort($v);
            return $res;
        };
        $L = $sumsByCount($left);
        $R = $sumsByCount($right);
        $ans = PHP_INT_MAX;
        for ($k = 0; $k <= $n; $k++) {
            foreach ($L[$k] as $s1) {
                $need = intdiv($total, 2) - $s1;
                $arr = $R[$n - $k];
                $lo = 0;
                $hi = count($arr);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($arr[$mid] < $need) $lo = $mid + 1;
                    else $hi = $mid;
                }
                foreach ([$lo - 1, $lo] as $j) {
                    if ($j >= 0 && $j < count($arr)) {
                        $s2 = $arr[$j];
                        $ans = min($ans, abs($total - 2 * ($s1 + $s2)));
                    }
                }
            }
        }
        return $ans;
    }
}
