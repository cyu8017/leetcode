<?php
class Solution {
    function maxArea($h, $w, $horizontalCuts, $verticalCuts) {
        $hs = array_merge([0, $h], $horizontalCuts);
        $vs = array_merge([0, $w], $verticalCuts);
        sort($hs);
        sort($vs);
        $maxH = 0;
        for ($i = 1; $i < count($hs); $i++) $maxH = max($maxH, $hs[$i] - $hs[$i - 1]);
        $maxV = 0;
        for ($i = 1; $i < count($vs); $i++) $maxV = max($maxV, $vs[$i] - $vs[$i - 1]);
        return ($maxH * $maxV) % 1000000007;
    }
}
