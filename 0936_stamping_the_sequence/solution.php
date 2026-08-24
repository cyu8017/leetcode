<?php
// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

class Solution {
    function movesToStamp($stamp, $target) {
        $m = strlen($stamp);
        $n = strlen($target);
        $arr = str_split($target);
        $done = array_fill(0, $n - $m + 1, false);
        $ans = [];
        $remaining = $n;
        $canStamp = function ($i) use (&$arr, $stamp, $m) {
            $changed = false;
            for ($j = 0; $j < $m; $j++) {
                if ($arr[$i + $j] === "?") continue;
                if ($arr[$i + $j] !== $stamp[$j]) return false;
                $changed = true;
            }
            return $changed;
        };
        $doStamp = function ($i) use (&$arr, $m) {
            $count = 0;
            for ($j = 0; $j < $m; $j++) {
                if ($arr[$i + $j] !== "?") {
                    $arr[$i + $j] = "?";
                    $count++;
                }
            }
            return $count;
        };
        while ($remaining > 0) {
            $stamped = false;
            for ($i = 0; $i <= $n - $m; $i++) {
                if (!$done[$i] && $canStamp($i)) {
                    $remaining -= $doStamp($i);
                    $ans[] = $i;
                    $done[$i] = true;
                    $stamped = true;
                    if ($remaining === 0) break;
                }
            }
            if (!$stamped) return [];
        }
        return array_reverse($ans);
    }
}
