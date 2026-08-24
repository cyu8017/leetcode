<?php
// LeetCode 3811 - Number of Alternating XOR Partitions
// https://leetcode.com/problems/number-of-alternating-xor-partitions/

class Solution {
    function alternatingXOR($nums, $target1, $target2) {
        $MOD = 1000000007;
        $cnt1 = [];
        $cnt2 = [];
        $cnt2[0] = 1;
        $pre = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $pre ^= $x;
            $a = isset($cnt2[$pre ^ $target1]) ? $cnt2[$pre ^ $target1] : 0;
            $b = isset($cnt1[$pre ^ $target2]) ? $cnt1[$pre ^ $target2] : 0;
            $ans = ($a + $b) % $MOD;
            if (!isset($cnt1[$pre])) $cnt1[$pre] = 0;
            $cnt1[$pre] = ($cnt1[$pre] + $a) % $MOD;
            if (!isset($cnt2[$pre])) $cnt2[$pre] = 0;
            $cnt2[$pre] = ($cnt2[$pre] + $b) % $MOD;
        }
        return $ans;
    }
}
