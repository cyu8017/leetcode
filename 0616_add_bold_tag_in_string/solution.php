<?php
// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

class Solution {
    function addBoldTag($s, $words) {
        $n = strlen($s);
        $bold = array_fill(0, $n, false);
        foreach ($words as $word) {
            $start = strpos($s, $word);
            while ($start !== false) {
                for ($i = $start; $i < $start + strlen($word); ++$i) $bold[$i] = true;
                $start = strpos($s, $word, $start + 1);
            }
        }
        $parts = "";
        $i = 0;
        while ($i < $n) {
            if ($bold[$i]) {
                $parts .= "<b>";
                while ($i < $n && $bold[$i]) $parts .= $s[$i++];
                $parts .= "</b>";
            } else {
                $parts .= $s[$i++];
            }
        }
        return $parts;
    }
}
