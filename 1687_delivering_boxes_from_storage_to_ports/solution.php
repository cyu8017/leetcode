<?php
// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

class Solution {
    function boxDelivering($boxes, $portsCount, $maxBoxes, $maxWeight) {
        $n = count($boxes);
        $w = array_fill(0, $n + 1, 0);
        $changes = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $w[$i] = $w[$i - 1] + $boxes[$i - 1][1];
            $changes[$i] = $changes[$i - 1] + ($i > 1 && $boxes[$i - 1][0] != $boxes[$i - 2][0] ? 1 : 0);
        }
        $dp = array_fill(0, $n + 1, 0);
        $q = [0];
        $qi = 0;
        for ($i = 1; $i <= $n; $i++) {
            while ($qi < count($q) && ($i - $q[$qi] > $maxBoxes || $w[$i] - $w[$q[$qi]] > $maxWeight)) $qi++;
            $j = $q[$qi];
            $dp[$i] = $dp[$j] + $changes[$i] - $changes[$j + 1] + 2;
            if ($i < $n) {
                $val = $dp[$i] - $changes[$i + 1];
                while (count($q) > $qi && $dp[$q[count($q) - 1]] - $changes[$q[count($q) - 1] + 1] >= $val) {
                    array_pop($q);
                }
                $q[] = $i;
            }
        }
        return $dp[$n];
    }
}
