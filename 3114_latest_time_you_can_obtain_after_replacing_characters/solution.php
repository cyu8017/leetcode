<?php
// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution {
    function findLatestTime($s) {
        for ($h = 11; ; $h--) {
            for ($m = 59; $m >= 0; $m--) {
                $t = str_pad((string)$h, 2, "0", STR_PAD_LEFT) . ":" . str_pad((string)$m, 2, "0", STR_PAD_LEFT);
                $ok = true;
                for ($i = 0; $i < 5; $i++) {
                    if ($s[$i] !== "?" && $s[$i] !== $t[$i]) { $ok = false; break; }
                }
                if ($ok) return $t;
            }
        }
    }
}
