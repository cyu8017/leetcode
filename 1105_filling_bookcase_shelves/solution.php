<?php
// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

class Solution {
    /**
     * @param Integer[][] $books
     * @param Integer $shelfWidth
     * @return Integer
     */
    function minHeightShelves($books, $shelfWidth) {
        $n = count($books);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $width = 0;
            $height = 0;
            $dp[$i] = PHP_INT_MAX;
            for ($j = $i; $j >= 1; $j--) {
                $w = $books[$j - 1][0];
                $h = $books[$j - 1][1];
                $width += $w;
                if ($width > $shelfWidth) break;
                $height = max($height, $h);
                $dp[$i] = min($dp[$i], $dp[$j - 1] + $height);
            }
        }
        return $dp[$n];
    }
}
