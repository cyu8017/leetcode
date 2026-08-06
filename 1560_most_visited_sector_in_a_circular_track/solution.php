<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $rounds
     * @return Integer[]
     */
    function mostVisited($n, $rounds) {
        $start = $rounds[0];
        $end = $rounds[count($rounds) - 1];
        if ($start <= $end) {
            return range($start, $end);
        }
        return array_merge(range(1, $end), range($start, $n));
    }
}
