<?php
class Solution {
    function daysBetweenDates($date1, $date2) {
        $t1 = strtotime($date1);
        $t2 = strtotime($date2);
        return intval(abs($t1 - $t2) / 86400);
    }
}
