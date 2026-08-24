<?php
// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

class BITI {
    public $n;
    public $c;
    function __construct($n_) {
        $this->n = $n_;
        $this->c = array_fill(0, $n_ + 1, 0);
    }
    function upd($x, $d) {
        for (; $x <= $this->n; $x += $x & -$x) $this->c[$x] += $d;
    }
    function qry($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->c[$x];
        return $s;
    }
}

class BITL {
    public $n;
    public $c;
    function __construct($n_) {
        $this->n = $n_;
        $this->c = array_fill(0, $n_ + 1, 0);
    }
    function upd($x, $d) {
        for (; $x <= $this->n; $x += $x & -$x) $this->c[$x] += $d;
    }
    function qry($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->c[$x];
        return $s;
    }
}

class Solution {
    private function kth($cnt, $m, $k) {
        $idx = 0;
        for ($bit = 1 << 20; $bit !== 0; $bit >>= 1) {
            $nidx = $idx + $bit;
            if ($nidx <= $m && $cnt->c[$nidx] < $k) {
                $k -= $cnt->c[$nidx];
                $idx = $nidx;
            }
        }
        return $idx + 1;
    }

    private function sumSmallest($cnt, $sum, $uniq, $m, $kk) {
        if ($kk <= 0) return 0;
        $r = $this->kth($cnt, $m, $kk);
        $before = $cnt->qry($r - 1);
        $s = $sum->qry($r - 1);
        $s += ($kk - $before) * $uniq[$r - 1];
        return $s;
    }

    private function lowerBound($arr, $x) {
        $lo = 0;
        $hi = count($arr);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($arr[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    function minimumCost($nums, $k, $dist) {
        $k--;
        $n = count($nums);
        $uniq = $nums;
        sort($uniq);
        $write = 0;
        $tmp = [];
        for ($i = 0; $i < count($uniq); $i++) {
            if ($write === 0 || $uniq[$i] !== $tmp[$write - 1]) {
                $tmp[] = $uniq[$i];
                $write++;
            }
        }
        $uniq = $tmp;
        $m = count($uniq);
        $cnt = new BITI($m + 2);
        $sum = new BITL($m + 2);
        for ($i = 1; $i <= min($dist + 1, $n - 1); $i++) {
            $r = $this->lowerBound($uniq, $nums[$i]) + 1;
            $cnt->upd($r, 1);
            $sum->upd($r, $nums[$i]);
        }
        $end = min($dist + 1, $n - 1);
        $kk = min($k, $end);
        $ans = $nums[0] + $this->sumSmallest($cnt, $sum, $uniq, $m, $kk);
        for ($i = $dist + 2; $i < $n; $i++) {
            $rem = $nums[$i - $dist - 1];
            $r1 = $this->lowerBound($uniq, $rem) + 1;
            $cnt->upd($r1, -1);
            $sum->upd($r1, -$rem);
            $add = $nums[$i];
            $r2 = $this->lowerBound($uniq, $add) + 1;
            $cnt->upd($r2, 1);
            $sum->upd($r2, $add);
            $kk = min($k, $dist + 1);
            $ans = min($ans, $nums[0] + $this->sumSmallest($cnt, $sum, $uniq, $m, $kk));
        }
        return $ans;
    }
}
