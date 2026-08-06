<?php
class Solution {
    function xorQueries($arr, $queries) {
        $prefix = [0];
        foreach ($arr as $value) $prefix[] = $prefix[count($prefix) - 1] ^ $value;
        $answer = [];
        foreach ($queries as $q) {
            $answer[] = $prefix[$q[1] + 1] ^ $prefix[$q[0]];
        }
        return $answer;
    }
}
