<?php
// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

class Solution {
    public $nums;
    public $k;
    public $m;
    function f($lim) {
        $cnt = [];
        $ans = 0;
        $l = 0;
        $t = 0;
        foreach ($this->nums as $x) {
            $c = ($cnt[$x] ?? 0) + 1;
            $cnt[$x] = $c;
            if ($c === $this->m) $t++;
            while (count($cnt) >= $lim && $t >= $this->k) {
                $y = $this->nums[$l++];
                $cy = $cnt[$y] - 1;
                if ($cy === $this->m - 1) $t--;
                if ($cy === 0) unset($cnt[$y]);
                else $cnt[$y] = $cy;
            }
            $ans += $l;
        }
        return $ans;
    }
    function countSubarrays($nums, $k, $m) {
        $this->nums = $nums;
        $this->k = $k;
        $this->m = $m;
        return $this->f($k) - $this->f($k + 1);
    }
}
