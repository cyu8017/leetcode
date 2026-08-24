<?php
// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

class Solution {
    function maxTotalValue($nums, $s) {
        $answer = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; ) {
            if ($s[$i] == '0') { $i++; continue; }
            $start = $i;
            while ($i < $n && $s[$i] == '1') $i++;
            $end = $i - 1;
            if ($start == 0) {
                for ($index = $start; $index <= $end; $index++) $answer += $nums[$index];
                continue;
            }
            $minimum = $nums[$start - 1];
            $total = 0;
            for ($index = $start - 1; $index <= $end; $index++) {
                $total += $nums[$index];
                if ($nums[$index] < $minimum) $minimum = $nums[$index];
            }
            $answer += $total - $minimum;
        }
        return $answer;
    }
}
