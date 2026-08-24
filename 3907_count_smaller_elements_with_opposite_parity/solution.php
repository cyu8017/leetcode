<?php
// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

class BIT3907 {
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
    function countSmallerOppositeParity($nums) {
        $n = count($nums);
        $sorted = $nums;
        sort($sorted);
        $m = 0;
        $uniq = [];
        for ($i = 0; $i < count($sorted); $i++) {
            if ($i === 0 || $sorted[$i] !== $sorted[$i - 1]) $uniq[$m++] = $sorted[$i];
        }
        $sorted = $uniq;
        $bits = [new BIT3907($m), new BIT3907($m)];
        $ans = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $lo = 0;
            $hi = count($sorted);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($sorted[$mid] < $nums[$i]) $lo = $mid + 1;
                else $hi = $mid;
            }
            $x = $lo + 1;
            $ans[$i] = $bits[($nums[$i] & 1) ^ 1]->query($x - 1);
            $bits[$nums[$i] & 1]->update($x, 1);
        }
        return $ans;
    }
}
