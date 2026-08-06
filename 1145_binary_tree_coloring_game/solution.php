<?php
// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class Solution {
    private $left = 0;
    private $right = 0;

    /**
     * @param TreeNode $root
     * @param Integer $n
     * @param Integer $x
     * @return Boolean
     */
    function btreeGameWinningMove($root, $n, $x) {
        $this->left = $this->right = 0;
        $this->dfs($root, $x);
        return max($this->left, $this->right, $n - $this->left - $this->right - 1) > intdiv($n, 2);
    }

    private function dfs($node, $x) {
        if ($node === null) return 0;
        $l = $this->dfs($node->left, $x);
        $r = $this->dfs($node->right, $x);
        if ($node->val === $x) {
            $this->left = $l;
            $this->right = $r;
        }
        return $l + $r + 1;
    }
}
