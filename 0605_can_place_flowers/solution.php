<?php
// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

class Solution {
    function canPlaceFlowers($flowerbed, $n) {
        if ($n === 0) return true;
        for ($i = 0; $i < count($flowerbed); ++$i) {
            if ($flowerbed[$i] === 1) continue;
            $leftEmpty = $i === 0 || $flowerbed[$i - 1] === 0;
            $rightEmpty = $i === count($flowerbed) - 1 || $flowerbed[$i + 1] === 0;
            if ($leftEmpty && $rightEmpty) {
                $flowerbed[$i] = 1;
                --$n;
                if ($n === 0) return true;
            }
        }
        return false;
    }
}
