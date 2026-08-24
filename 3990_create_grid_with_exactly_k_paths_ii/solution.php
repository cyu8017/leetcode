<?php
// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

class Solution {
    function createGrid($k) {
        if ($k <= 0) return [];
        $l = $this->bitWidth($k);
        $m = 2 * $l;
        $n = $l + 3;
        $result = [];
        for ($i = 0; $i < $m; $i++) $result[] = str_repeat('#', $n);
        for ($i = 0; $i < $l; $i++) {
            $r = 2 * $i;
            $row0 = str_split($result[$r]);
            $row1 = str_split($result[$r + 1]);
            $row0[$i] = $row0[$i + 1] = $row1[$i] = $row1[$i + 1] = '.';
            if (($k & (1 << $i)) != 0) {
                for ($c = $i + 2; $c < $n; $c++) $row0[$c] = '.';
            }
            $result[$r] = implode('', $row0);
            $result[$r + 1] = implode('', $row1);
        }
        for ($r = 0; $r < $m; $r++) {
            $row = str_split($result[$r]);
            $row[$n - 1] = '.';
            $result[$r] = implode('', $row);
        }
        return $result;
    }

    private function bitWidth($k) {
        $w = 0;
        while ($k != 0) { $w++; $k >>= 1; }
        return $w;
    }
}
