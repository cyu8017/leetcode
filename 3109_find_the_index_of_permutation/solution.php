<?php
// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

class BIT {
    public $n;
    public $c;
    function __construct($n) {
        $this->n = $n;
        $this->c = array_fill(0, $n + 1, 0);
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
    function getPermutationIndex($perm) {
        $MOD = 1000000007;
        $n = count($perm);
        $tree = new BIT($n + 1);
        $f = array_fill(0, $n, 0);
        $f[0] = 1;
        for ($i = 1; $i < $n; $i++) $f[$i] = $f[$i - 1] * $i % $MOD;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $x = $perm[$i];
            $cnt = $x - 1 - $tree->query($x);
            $ans = ($ans + $cnt * $f[$n - 1 - $i]) % $MOD;
            $tree->update($x, 1);
        }
        return $ans;
    }
}
