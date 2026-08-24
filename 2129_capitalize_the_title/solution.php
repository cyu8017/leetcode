<?php
// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

class Solution {
    /**
     * @param String $title
     * @return String
     */
    function capitalizeTitle($title) {
        $parts = preg_split('/\s+/', trim($title));
        for ($i = 0; $i < count($parts); $i++) {
            $w = strtolower($parts[$i]);
            if (strlen($w) > 2) $w = strtoupper($w[0]) . substr($w, 1);
            $parts[$i] = $w;
        }
        return implode(' ', $parts);
    }
}
