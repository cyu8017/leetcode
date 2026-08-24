<?php
// LeetCode 3777 - Minimum Deletions to Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class _MDBIT {
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
    function minDeletions($s, $queries) {
        $n = strlen($s);
        $nums = array_fill(0, $n, 0);
        $bit = new _MDBIT($n);
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] === $s[$i - 1]) {
                $nums[$i] = 1;
                $bit->update($i + 1, 1);
            }
        }
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $j = $q[1];
                $delta = ($nums[$j] ^ 1) - $nums[$j];
                $nums[$j] ^= 1;
                $bit->update($j + 1, $delta);
                if ($j + 1 < $n) {
                    $delta = ($nums[$j + 1] ^ 1) - $nums[$j + 1];
                    $nums[$j + 1] ^= 1;
                    $bit->update($j + 2, $delta);
                }
            } else {
                $l = $q[1];
                $r = $q[2];
                $ans[] = $bit->query($r + 1) - $bit->query($l + 1);
            }
        }
        return $ans;
    }
}
