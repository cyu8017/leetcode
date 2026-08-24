<?php
// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

class Solution {
    private $bit;

    private function add($i, $v) {
        $n = count($this->bit);
        for (; $i < $n; $i += $i & -$i) $this->bit[$i] += $v;
    }

    private function sum($i) {
        $s = 0;
        for (; $i > 0; $i -= $i & -$i) $s += $this->bit[$i];
        return $s;
    }

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function goodTriplets($nums1, $nums2) {
        $n = count($nums1);
        $pos2 = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $pos2[$nums2[$i]] = $i;
        $mapped = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $mapped[$i] = $pos2[$nums1[$i]];
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $this->bit = array_fill(0, $n + 2, 0);
        for ($i = 0; $i < $n; $i++) {
            $left[$i] = $this->sum($mapped[$i]);
            $this->add($mapped[$i] + 1, 1);
        }
        $this->bit = array_fill(0, $n + 2, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $right[$i] = $this->sum($n) - $this->sum($mapped[$i] + 1);
            $this->add($mapped[$i] + 1, 1);
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) $ans += $left[$i] * $right[$i];
        return $ans;
    }
}
