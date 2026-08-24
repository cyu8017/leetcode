<?php
// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution {
    function toBin($x) {
        if ($x === 0) return '0';
        $s = '';
        while ($x > 0) {
            $s = strval($x & 1) . $s;
            $x >>= 1;
        }
        return $s;
    }

    function perm($i, &$idx, $bs, &$ans) {
        if ($i === 3) {
            $s = $bs[$idx[0]] . $bs[$idx[1]] . $bs[$idx[2]];
            $v = 0;
            $len = strlen($s);
            for ($p = 0; $p < $len; $p++) $v = $v * 2 + (ord($s[$p]) - 48);
            if ($v > $ans[0]) $ans[0] = $v;
            return;
        }
        for ($j = $i; $j < 3; $j++) {
            $t = $idx[$i]; $idx[$i] = $idx[$j]; $idx[$j] = $t;
            $this->perm($i + 1, $idx, $bs, $ans);
            $t = $idx[$i]; $idx[$i] = $idx[$j]; $idx[$j] = $t;
        }
    }

    function maxGoodNumber($nums) {
        $bs = [$this->toBin($nums[0]), $this->toBin($nums[1]), $this->toBin($nums[2])];
        $idx = [0, 1, 2];
        $ans = [0];
        $this->perm(0, $idx, $bs, $ans);
        return $ans[0];
    }
}
