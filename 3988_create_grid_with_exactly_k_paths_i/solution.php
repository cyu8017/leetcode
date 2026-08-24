<?php
// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

class Solution {
    function createGrid($m, $n, $k) {
        $cands = [];
        if ($k === 1) $cands[] = ["."];
        else if ($k === 2) $cands[] = ["..", ".."];
        else if ($k === 3) {
            $cands[] = ["..", "..", ".."];
            $cands[] = ["...", "..."];
        } else if ($k === 4) {
            $cands[] = ["..", "..", "..", ".."];
            $cands[] = ["....", "...."];
            $cands[] = ["..#", "...", "#.."];
        }
        foreach ($cands as $pat) {
            $pr = count($pat);
            $pc = strlen($pat[0]);
            if ($pr > $m || $pc > $n) continue;
            $result = array_fill(0, $m, str_repeat('#', $n));
            for ($i = 0; $i < $pr; $i++) {
                $row = str_split($result[$i]);
                for ($j = 0; $j < $pc; $j++) $row[$j] = $pat[$i][$j];
                $result[$i] = implode('', $row);
            }
            for ($i = $pr; $i < $m; $i++) {
                $row = str_split($result[$i]);
                $row[$pc - 1] = '.';
                $result[$i] = implode('', $row);
            }
            for ($j = $pc; $j < $n; $j++) {
                $row = str_split($result[$m - 1]);
                $row[$j] = '.';
                $result[$m - 1] = implode('', $row);
            }
            return $result;
        }
        return [];
    }
}
