<?php

class Solution {
    /**
     * @param Integer[] $boxes
     * @param Integer[] $warehouse
     * @return Integer
     */
    function maxBoxesInWarehouse($boxes, $warehouse) {
        $n = count($warehouse);
        $left = $warehouse;
        $right = $warehouse;
        for ($i = 1; $i < $n; $i++) {
            $left[$i] = min($left[$i], $left[$i - 1]);
        }
        for ($i = $n - 2; $i >= 0; $i--) {
            $right[$i] = min($right[$i], $right[$i + 1]);
        }
        $capacity = [];
        for ($i = 0; $i < $n; $i++) {
            $capacity[] = max($left[$i], $right[$i]);
        }
        sort($capacity);
        sort($boxes);
        $i = 0;
        $m = count($boxes);
        foreach ($capacity as $room) {
            if ($i < $m && $boxes[$i] <= $room) {
                $i++;
            }
        }
        return $i;
    }
}
