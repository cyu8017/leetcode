<?php
// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution {
    function kthGrammar($n, $k) {
        if ($n === 1) return 0;
        $mid = 1 << ($n - 2);
        if ($k <= $mid) return $this->kthGrammar($n - 1, $k);
        return 1 - $this->kthGrammar($n - 1, $k - $mid);
    }
}
