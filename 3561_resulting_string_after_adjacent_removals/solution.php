<?php
// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

class Solution {
    private function isContiguous($a, $b) {
        $x = abs(ord($a) - ord($b));
        return $x === 1 || $x === 25;
    }

    function resultingString($s) {
        $stk = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (count($stk) > 0 && $this->isContiguous($stk[count($stk) - 1], $c))
                array_pop($stk);
            else $stk[] = $c;
        }
        return implode('', $stk);
    }
}
