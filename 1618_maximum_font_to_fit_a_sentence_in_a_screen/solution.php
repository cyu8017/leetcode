<?php
// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

class FontInfo {
    function getWidth($fontSize, $ch) {
        return $fontSize;
    }

    function getHeight($fontSize) {
        return $fontSize;
    }
}

class Solution {
    /**
     * @param String $text
     * @param Integer $w
     * @param Integer $h
     * @param Integer[] $fonts
     * @param FontInfo|null $fontInfo
     * @return Integer
     */
    function maxFont($text, $w, $h, $fonts, $fontInfo = null) {
        $fontInfo = $fontInfo ?: new FontInfo();
        $lo = 0;
        $hi = count($fonts) - 1;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $f = $fonts[$mid];
            $width = 0;
            $len = strlen($text);
            for ($i = 0; $i < $len; $i++) {
                $width += $fontInfo->getWidth($f, $text[$i]);
            }
            $fits = $fontInfo->getHeight($f) <= $h && $width <= $w;
            if ($fits) {
                $ans = $f;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $ans;
    }
}
