<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequence($s) {
        $first = [];
        $last = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (!isset($first[$c])) {
                $first[$c] = $i;
            }
            $last[$c] = $i;
        }
        $ans = 0;
        foreach ($first as $c => $fi) {
            $li = $last[$c];
            if ($li - $fi > 1) {
                $mid = [];
                for ($i = $fi + 1; $i < $li; $i++) {
                    $mid[$s[$i]] = true;
                }
                $ans += count($mid);
            }
        }
        return $ans;
    }
}
