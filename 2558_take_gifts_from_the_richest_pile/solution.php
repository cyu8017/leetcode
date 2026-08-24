<?php
// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution {
    function pickGifts($gifts, $k) {
        $h = new SplPriorityQueue();
        foreach ($gifts as $g) $h->insert($g, $g);
        for ($i = 0; $i < $k; $i++) {
            $x = $h->extract();
            $nxt = (int)floor(sqrt($x));
            $h->insert($nxt, $nxt);
        }
        $ans = 0;
        while (!$h->isEmpty()) $ans += $h->extract();
        return $ans;
    }
}
