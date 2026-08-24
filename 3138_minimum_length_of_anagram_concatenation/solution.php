<?php
// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution {
    public $s;
    public $n;
    public $cnt;
    function minAnagramLength($s) {
        $this->s = $s;
        $this->n = strlen($s);
        $this->cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $this->n; $i++) $this->cnt[ord($s[$i]) - 97]++;
        for ($i = 1; ; $i++) {
            if ($this->n % $i === 0 && $this->check($i)) return $i;
        }
    }
    function check($k) {
        $n = $this->n;
        $s = $this->s;
        for ($i = 0; $i < $n; $i += $k) {
            $cnt1 = array_fill(0, 26, 0);
            for ($j = $i; $j < $i + $k; $j++) $cnt1[ord($s[$j]) - 97]++;
            for ($j = 0; $j < 26; $j++) {
                if ($cnt1[$j] * intdiv($n, $k) !== $this->cnt[$j]) return false;
            }
        }
        return true;
    }
}
