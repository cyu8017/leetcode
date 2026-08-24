<?php
// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

class Solution {
    function tripletCount($a, $b, $c) {
        $cnt1 = [0, 0];
        $cnt2 = [0, 0];
        $cnt3 = [0, 0];
        foreach ($a as $x) $cnt1[$this->bitCount($x) % 2]++;
        foreach ($b as $x) $cnt2[$this->bitCount($x) % 2]++;
        foreach ($c as $x) $cnt3[$this->bitCount($x) % 2]++;
        $ans = 0;
        for ($i = 0; $i < 2; $i++)
            for ($j = 0; $j < 2; $j++)
                for ($k = 0; $k < 2; $k++)
                    if (($i + $j + $k) % 2 === 0) $ans += $cnt1[$i] * $cnt2[$j] * $cnt3[$k];
        return $ans;
    }

    private function bitCount($x) {
        $n = 0;
        while ($x) { $n += $x & 1; $x >>= 1; }
        return $n;
    }
}
