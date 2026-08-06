<?php
class Solution {
    function stringShift($s, $shift) {
        $offset = 0;
        foreach ($shift as [$direction, $amount]) {
            $offset += $direction ? $amount : -$amount;
        }
        $n = strlen($s);
        $offset %= $n;
        if ($offset < 0) $offset += $n;
        if (!$offset) return $s;
        return substr($s, -$offset) . substr($s, 0, $n - $offset);
    }
}
