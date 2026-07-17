<?php
// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function splitString($s) {
        return $this->dfs($s, 0, null, 0);
    }

    /**
     * @param string $s
     * @param int $index
     * @param int|null $previous
     * @param int $parts
     * @return bool
     */
    private function dfs($s, $index, $previous, $parts) {
        $n = strlen($s);
        if ($index === $n) {
            return $parts >= 2;
        }

        for ($end = $index + 1; $end <= $n; $end++) {
            $value = (int)substr($s, $index, $end - $index);
            if ($previous === null) {
                if ($this->dfs($s, $end, $value, $parts + 1)) {
                    return true;
                }
            } elseif ($value === $previous - 1) {
                if ($this->dfs($s, $end, $value, $parts + 1)) {
                    return true;
                }
            } elseif ($value > $previous - 1) {
                break;
            }
        }

        return false;
    }
}
