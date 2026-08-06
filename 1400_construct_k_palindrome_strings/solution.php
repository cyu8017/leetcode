<?php
class Solution {
    function canConstruct($s, $k) {
        if ($k > strlen($s)) return false;
        $c = array_count_values(str_split($s));
        $odd = 0;
        foreach ($c as $v) if ($v % 2) $odd++;
        return $odd <= $k;
    }
}
