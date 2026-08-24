<?php
// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution {
    function takeCharacters($s, $k) {
        $n = strlen($s);
        $cnt = [0, 0, 0];
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        if ($cnt[0] < $k || $cnt[1] < $k || $cnt[2] < $k) return -1;
        $need = [$cnt[0] - $k, $cnt[1] - $k, $cnt[2] - $k];
        $window = [0, 0, 0];
        $left = 0;
        $maxMid = 0;
        for ($right = 0; $right < $n; $right++) {
            $window[ord($s[$right]) - 97]++;
            while ($window[0] > $need[0] || $window[1] > $need[1] || $window[2] > $need[2]) {
                $window[ord($s[$left]) - 97]--;
                $left++;
            }
            if ($right - $left + 1 > $maxMid) $maxMid = $right - $left + 1;
        }
        return $n - $maxMid;
    }
}
