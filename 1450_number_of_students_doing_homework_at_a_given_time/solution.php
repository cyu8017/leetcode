<?php
class Solution {
    function busyStudent($startTime, $endTime, $queryTime) {
        $ans = 0;
        foreach ($startTime as $i => $start) {
            if ($start <= $queryTime && $queryTime <= $endTime[$i]) $ans++;
        }
        return $ans;
    }
}
