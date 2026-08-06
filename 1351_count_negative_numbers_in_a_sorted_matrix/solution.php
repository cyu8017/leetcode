<?php
class Solution {
    function countNegatives($grid) {
        $answer = 0;
        foreach ($grid as $row) {
            $n = count($row);
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($row[$mid] < 0) $hi = $mid;
                else $lo = $mid + 1;
            }
            $answer += $n - $lo;
        }
        return $answer;
    }
}
