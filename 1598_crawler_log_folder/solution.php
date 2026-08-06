<?php

class Solution {
    /**
     * @param String[] $logs
     * @return Integer
     */
    function minOperations($logs) {
        $depth = 0;
        foreach ($logs as $log) {
            if ($log === '../') {
                $depth = max(0, $depth - 1);
            } elseif ($log !== './') {
                $depth++;
            }
        }
        return $depth;
    }
}
