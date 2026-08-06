<?php
class Solution {
    function numSteps($s) {
        $steps = 0;
        $carry = 0;
        for ($i = strlen($s) - 1; $i >= 1; $i--) {
            $value = intval($s[$i]) + $carry;
            if ($value === 1) {
                $steps += 2;
                $carry = 1;
            } else {
                $steps += 1;
            }
        }
        return $steps + $carry;
    }
}
