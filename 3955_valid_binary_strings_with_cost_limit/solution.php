<?php
// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

class Solution {
    function generateValidStrings($n, $k) {
        $ans = [];
        $this->dfs(0, 0, $n, $k, '', $ans);
        return $ans;
    }

    private function dfs($i, $tot, $n, $k, $path, &$ans) {
        if ($i >= $n) {
            $ans[] = $path;
            return;
        }
        $this->dfs($i + 1, $tot, $n, $k, $path . '0', $ans);
        if (($path === '' || $path[strlen($path) - 1] == '0') && $tot + $i <= $k) {
            $this->dfs($i + 1, $tot + $i, $n, $k, $path . '1', $ans);
        }
    }
}
