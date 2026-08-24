<?php
// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

class Solution {
    function longestBalanced($s) {
        $cnt0 = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '0') $cnt0++;
        $cnt1 = $n - $cnt0;
        $pos = [];
        $pos[0] = [-1];
        $ans = 0;
        $pre = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') $pre++;
            else $pre--;
            if (!isset($pos[$pre])) $pos[$pre] = [];
            $pos[$pre][] = $i;
            $ans = max($ans, $i - $pos[$pre][0]);
            if (isset($pos[$pre - 2])) {
                $p = $pos[$pre - 2];
                if (intdiv($i - $p[0] - 2, 2) < $cnt0) $ans = max($ans, $i - $p[0]);
                else if (count($p) > 1) $ans = max($ans, $i - $p[1]);
            }
            if (isset($pos[$pre + 2])) {
                $p = $pos[$pre + 2];
                if (intdiv($i - $p[0] - 2, 2) < $cnt1) $ans = max($ans, $i - $p[0]);
                else if (count($p) > 1) $ans = max($ans, $i - $p[1]);
            }
        }
        return $ans;
    }
}
