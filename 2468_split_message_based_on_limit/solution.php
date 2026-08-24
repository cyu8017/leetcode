<?php
// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

class Solution {
    function splitMessage($message, $limit) {
        $n = strlen($message);
        for ($parts = 1; $parts <= $n; $parts++) {
            $sbDigits = strlen((string)$parts);
            $ok = true;
            $idx = 0;
            $res = [];
            for ($i = 1; $i <= $parts; $i++) {
                $tail = 3 + strlen((string)$i) + $sbDigits;
                $cap = $limit - $tail;
                if ($cap <= 0 || $idx >= $n) { $ok = false; break; }
                $take = $cap;
                if ($take > $n - $idx) $take = $n - $idx;
                $res[] = substr($message, $idx, $take) . '<' . $i . '/' . $parts . '>';
                $idx += $take;
            }
            if ($ok && $idx === $n) return $res;
        }
        return [];
    }
}
