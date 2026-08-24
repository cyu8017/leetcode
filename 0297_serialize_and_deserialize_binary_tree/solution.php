<?php
// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

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

class Codec {
    /**
     * @param TreeNode|null $root
     * @return String
     */
    function serialize($root) {
        if ($root === null) {
            return "";
        }
        $values = [];
        $queue = [$root];
        while (count($queue) > 0) {
            $node = array_shift($queue);
            if ($node === null) {
                $values[] = "";
            } else {
                $values[] = (string)$node->val;
                $queue[] = $node->left;
                $queue[] = $node->right;
            }
        }
        while (count($values) > 0 && $values[count($values) - 1] === "") {
            array_pop($values);
        }
        return implode(",", $values);
    }

    /**
     * @param String $data
     * @return TreeNode|null
     */
    function deserialize($data) {
        if ($data === "") {
            return null;
        }
        $values = explode(",", $data);
        $root = new TreeNode((int)$values[0]);
        $queue = [$root];
        $index = 1;
        while (count($queue) > 0 && $index < count($values)) {
            $node = array_shift($queue);
            if ($index < count($values) && $values[$index] !== "") {
                $node->left = new TreeNode((int)$values[$index]);
                $queue[] = $node->left;
            }
            $index++;
            if ($index < count($values) && $values[$index] !== "") {
                $node->right = new TreeNode((int)$values[$index]);
                $queue[] = $node->right;
            }
            $index++;
        }
        return $root;
    }
}
