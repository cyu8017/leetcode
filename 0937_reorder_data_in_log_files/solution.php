<?php
// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

class Solution {
    function reorderLogFiles($logs) {
        $letter = [];
        $digit = [];
        foreach ($logs as $log) {
            $i = strpos($log, " ");
            $ch = $log[$i + 1];
            if ($ch >= "0" && $ch <= "9") $digit[] = $log;
            else $letter[] = $log;
        }
        usort($letter, function ($a, $b) {
            $ia = strpos($a, " ");
            $ib = strpos($b, " ");
            $ca = substr($a, $ia + 1);
            $cb = substr($b, $ib + 1);
            if ($ca !== $cb) return $ca < $cb ? -1 : 1;
            $ida = substr($a, 0, $ia);
            $idb = substr($b, 0, $ib);
            return $ida <=> $idb;
        });
        return array_merge($letter, $digit);
    }
}
