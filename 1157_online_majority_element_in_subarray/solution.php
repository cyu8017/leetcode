<?php
// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker {
    private $arr;
    private $pos = [];

    /**
     * @param Integer[] $arr
     */
    function __construct($arr) {
        $this->arr = $arr;
        foreach ($arr as $i => $x) {
            $this->pos[$x][] = $i;
        }
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @param Integer $threshold
     * @return Integer
     */
    function query($left, $right, $threshold) {
        $candidate = 0;
        $count = 0;
        for ($i = $left; $i <= $right; $i++) {
            if ($count === 0) $candidate = $this->arr[$i];
            $count += $this->arr[$i] === $candidate ? 1 : -1;
        }
        $locs = $this->pos[$candidate] ?? [];
        $lo = 0; $hi = count($locs);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($locs[$mid] < $left) $lo = $mid + 1;
            else $hi = $mid;
        }
        $L = $lo;
        $lo = 0; $hi = count($locs);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($locs[$mid] <= $right) $lo = $mid + 1;
            else $hi = $mid;
        }
        return ($lo - $L) >= $threshold ? $candidate : -1;
    }
}
