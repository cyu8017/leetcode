<?php
// LeetCode 0337 - House Robber III
// https://leetcode.com/problems/house-robber-iii/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    /**
     * @param TreeNode|array|null $root
     * @return Integer
     */
    function rob($root) {
        if (is_array($root)) {
            $root = $this->listToTree($root);
        }
        return max($this->dfs($root));
    }

    private function dfs($node) {
        if ($node === null) {
            return [0, 0];
        }

        [$leftWith, $leftWithout] = $this->dfs($node->left);
        [$rightWith, $rightWithout] = $this->dfs($node->right);

        $withRob = $node->val + $leftWithout + $rightWithout;
        $withoutRob = max($leftWith, $leftWithout) + max($rightWith, $rightWithout);
        return [$withRob, $withoutRob];
    }

    private function listToTree($values) {
        if ($values === null || count($values) === 0) {
            return null;
        }

        $root = new TreeNode($values[0]);
        $queue = [$root];
        $index = 1;
        $count = count($values);
        while ($index < $count) {
            $node = array_shift($queue);
            if ($index < $count && $values[$index] !== null) {
                $node->left = new TreeNode($values[$index]);
                $queue[] = $node->left;
            }
            $index++;
            if ($index < $count && $values[$index] !== null) {
                $node->right = new TreeNode($values[$index]);
                $queue[] = $node->right;
            }
            $index++;
        }
        return $root;
    }
}
