<?php
// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution {
    function generateTag($caption) {
        $ans = '#';
        $words = preg_split('/\s+/', trim($caption));
        $i = 0;
        foreach ($words as $word) {
            if ($word === '') continue;
            $w = strtolower($word);
            if ($i === 0) $ans .= $w;
            else {
                if (strlen($w) > 0) $w = strtoupper($w[0]) . substr($w, 1);
                $ans .= $w;
            }
            if (strlen($ans) >= 100) break;
            $i++;
        }
        if (strlen($ans) > 100) $ans = substr($ans, 0, 100);
        return $ans;
    }
}
