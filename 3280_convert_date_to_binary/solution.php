<?php
// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

class Solution {
    function convertDateToBinary($date) {
        $parts = explode('-', $date);
        $y = intval($parts[0]);
        $m = intval($parts[1]);
        $d = intval($parts[2]);
        return $this->toBinary($y) . '-' . $this->toBinary($m) . '-' . $this->toBinary($d);
    }

    private function toBinary($v) {
        if ($v === 0) return '0';
        $s = '';
        while ($v > 0) { $s = (($v & 1) ? '1' : '0') . $s; $v >>= 1; }
        return $s;
    }
}
