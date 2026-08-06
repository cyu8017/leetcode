<?php

class Solution {
    /**
     * @param Integer[] $boxes
     * @param Integer[] $warehouse
     * @return Integer
     */
    function maxBoxesInWarehouse($boxes, $warehouse) {
        for ($i = 1; $i < count($warehouse); $i++) {
            $warehouse[$i] = min($warehouse[$i], $warehouse[$i - 1]);
        }
        sort($boxes);
        $room = count($warehouse) - 1;
        $used = 0;
        foreach ($boxes as $box) {
            while ($room >= 0 && $warehouse[$room] < $box) {
                $room--;
            }
            if ($room < 0) {
                break;
            }
            $used++;
            $room--;
        }
        return $used;
    }
}
