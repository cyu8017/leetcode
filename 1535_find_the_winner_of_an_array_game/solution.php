<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function getWinner($arr, $k) {
        $champion = $arr[0];
        $wins = 0;
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $challenger = $arr[$i];
            if ($champion > $challenger) {
                $wins++;
            } else {
                $champion = $challenger;
                $wins = 1;
            }
            if ($wins === $k) {
                break;
            }
        }
        return $champion;
    }
}
