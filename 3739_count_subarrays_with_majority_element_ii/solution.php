<?php
// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class _CMBIT {
    public $n;
    public $c;
    function __construct($n_) {
        $this->n = $n_;
        $this->c = array_fill(0, $n_ + 1, 0);
    }
    function update($x, $delta) {
        for (; $x <= $this->n; $x += $x & -$x) $this->c[$x] += $delta;
    }
    function query($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->c[$x];
        return $s;
    }
}

class Solution {
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);
        $tree = new _CMBIT(2 * $n + 1);
        $s = $n + 1;
        $tree->update($s, 1);
        $ans = 0;
        foreach ($nums as $x) {
            if ($x === $target) $s++;
            else $s--;
            $ans += $tree->query($s - 1);
            $tree->update($s, 1);
        }
        return $ans;
    }
}
