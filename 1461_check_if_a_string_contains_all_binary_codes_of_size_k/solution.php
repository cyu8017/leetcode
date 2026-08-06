<?php
class Solution {
    function hasAllCodes($s, $k) {
        $seen = [];
        $n = strlen($s);
        for ($i = 0; $i <= $n - $k; $i++) $seen[substr($s, $i, $k)] = true;
        return count($seen) === (1 << $k);
    }
}
