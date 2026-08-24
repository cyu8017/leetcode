<?php
// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution {
    function canTransform($start, $result) {
        $a = '';
        $b = '';
        $n = strlen($start);
        for ($i = 0; $i < $n; $i++) if ($start[$i] !== 'X') $a .= $start[$i];
        $rn = strlen($result);
        for ($i = 0; $i < $rn; $i++) if ($result[$i] !== 'X') $b .= $result[$i];
        if ($a !== $b) return false;
        $i = 0;
        $j = 0;
        while ($i < $n && $j < $n) {
            while ($i < $n && $start[$i] === 'X') $i++;
            while ($j < $n && $result[$j] === 'X') $j++;
            if ($i === $n || $j === $n) break;
            if ($start[$i] !== $result[$j]) return false;
            if ($start[$i] === 'L' && $i < $j) return false;
            if ($start[$i] === 'R' && $i > $j) return false;
            $i++;
            $j++;
        }
        return true;
    }
}
