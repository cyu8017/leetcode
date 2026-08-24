<?php
// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

class Solution {
    function ipToCIDR($ip, $n) {
        $ipToInt = function ($value) {
            $result = 0;
            foreach (explode('.', $value) as $part) $result = $result * 256 + intval($part, 10);
            return $result;
        };
        $intToIp = function ($value) {
            return implode('.', [
                intdiv($value, 16777216) % 256,
                intdiv($value, 65536) % 256,
                intdiv($value, 256) % 256,
                $value % 256
            ]);
        };
        $bitLength = function ($value) {
            $len = 0;
            while ($value > 0) { $value = intdiv($value, 2); $len++; }
            return $len;
        };
        $start = $ipToInt($ip);
        $answer = [];
        while ($n > 0) {
            $lowbit = $start === 0 ? (1 << 32) : ($start & -$start);
            while ($lowbit > $n) $lowbit = intdiv($lowbit, 2);
            $mask = 32 - ($bitLength($lowbit) - 1);
            $answer[] = $intToIp($start) . '/' . $mask;
            $start += $lowbit;
            $n -= $lowbit;
        }
        return $answer;
    }
}
