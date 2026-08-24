<?php
// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

class Solution {
    function makeLargestSpecial($s) {
        $parts = [];
        $balance = 0;
        $start = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $balance += $s[$i] === '1' ? 1 : -1;
            if ($balance === 0) {
                $parts[] = '1' . $this->makeLargestSpecial(substr($s, $start + 1, $i - $start - 1)) . '0';
                $start = $i + 1;
            }
        }
        rsort($parts);
        return implode('', $parts);
    }
}
