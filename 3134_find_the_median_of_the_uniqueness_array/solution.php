<?php
// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

class Solution {
    public $nums;
    public $n;
    public $m;
    function medianOfUniquenessArray($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->m = (1 + $this->n) * $this->n / 2;
        $lo = 1;
        $hi = $this->n;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($this->check($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
    function check($mx) {
        $cnt = [];
        $l = 0;
        $k = 0;
        $n = $this->n;
        for ($r = 0; $r < $n; $r++) {
            $x = $this->nums[$r];
            $cnt[$x] = ($cnt[$x] ?? 0) + 1;
            while (count($cnt) > $mx) {
                $y = $this->nums[$l++];
                $nv = $cnt[$y] - 1;
                if ($nv === 0) unset($cnt[$y]);
                else $cnt[$y] = $nv;
            }
            $k += $r - $l + 1;
            if ($k >= intdiv($this->m + 1, 2)) return true;
        }
        return false;
    }
}
