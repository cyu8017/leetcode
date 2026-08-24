<?php
// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

class Solution {
    private $sl;
    private $keys;

    private function add($v) {
        if (!isset($this->sl[$v])) {
            $this->sl[$v] = 0;
            $lo = 0;
            $hi = count($this->keys);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($this->keys[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($this->keys, $lo, 0, [$v]);
        }
        $this->sl[$v]++;
    }

    private function rem($v) {
        $c = $this->sl[$v] - 1;
        if ($c === 0) {
            unset($this->sl[$v]);
            $ix = array_search($v, $this->keys, true);
            if ($ix !== false) array_splice($this->keys, $ix, 1);
        } else $this->sl[$v] = $c;
    }

    function countPartitions($nums, $k) {
        $mod = 1000000007;
        $this->sl = [];
        $this->keys = [];
        $n = count($nums);
        $f = array_fill(0, $n + 1, 0);
        $g = array_fill(0, $n + 1, 0);
        $f[0] = $g[0] = 1;
        for ($l = 1, $r = 1; $r <= $n; $r++) {
            $this->add($nums[$r - 1]);
            while ($this->keys[count($this->keys) - 1] - $this->keys[0] > $k) {
                $this->rem($nums[$l - 1]);
                $l++;
            }
            $f[$r] = $g[$r - 1];
            if ($l >= 2) $f[$r] = ($f[$r] - $g[$l - 2] + $mod) % $mod;
            $g[$r] = ($g[$r - 1] + $f[$r]) % $mod;
        }
        return $f[$n];
    }
}
