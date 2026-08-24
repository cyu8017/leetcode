<?php
// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

class Solution {
    function minSwapsCouples($row) {
        $pos = [];
        $n = count($row);
        for ($i = 0; $i < $n; $i++) $pos[$row[$i]] = $i;
        $swaps = 0;
        for ($i = 0; $i < $n; $i += 2) {
            $partner = $row[$i] ^ 1;
            if ($row[$i + 1] === $partner) continue;
            $j = $pos[$partner];
            $pos[$row[$i + 1]] = $j;
            $row[$j] = $row[$i + 1];
            $row[$i + 1] = $partner;
            $pos[$partner] = $i + 1;
            $swaps++;
        }
        return $swaps;
    }
}
