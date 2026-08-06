<?php
class Solution {
    function minStartValue($nums) {
        $prefix = 0;
        $lowest = 0;
        foreach ($nums as $value) {
            $prefix += $value;
            $lowest = min($lowest, $prefix);
        }
        return 1 - $lowest;
    }
}
