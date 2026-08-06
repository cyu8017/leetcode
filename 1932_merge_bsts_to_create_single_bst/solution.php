<?php
class Solution {
    /**
     * @param TreeNode[]|array $trees
     * @return TreeNode|null
     */
    function canMerge($trees) {
        $trees = array_map(function ($t) {
            return is_array($t) ? $this->listToTree($t) : $t;
        }, $trees);

        $valueToRoot = [];
        $count = [];
        foreach ($trees as $tree) {
            $valueToRoot[$tree->val] = $tree;
            $count[$tree->val] = ($count[$tree->val] ?? 0) + 1;
            if ($tree->left !== null) {
                $count[$tree->left->val] = ($count[$tree->left->val] ?? 0) + 1;
            }
            if ($tree->right !== null) {
                $count[$tree->right->val] = ($count[$tree->right->val] ?? 0) + 1;
            }
        }

        $root = null;
        foreach ($trees as $t) {
            if (($count[$t->val] ?? 0) === 1) {
                if ($root !== null) {
                    return null;
                }
                $root = $t;
            }
        }
        if ($root === null) {
            return null;
        }

        unset($valueToRoot[$root->val]);
        if (!$this->merge($root, $valueToRoot) || !empty($valueToRoot)) {
            return null;
        }
        return $this->isValidBST($root, PHP_INT_MIN, PHP_INT_MAX) ? $root : null;
    }

    private function listToTree($values) {
        if ($values === null || count($values) === 0) {
            return null;
        }
        $root = (object)['val' => $values[0], 'left' => null, 'right' => null];
        $queue = [$root];
        $index = 1;
        while (count($queue) > 0 && $index < count($values)) {
            $node = array_shift($queue);
            if ($index < count($values)) {
                if ($values[$index] !== null) {
                    $node->left = (object)['val' => $values[$index], 'left' => null, 'right' => null];
                    $queue[] = $node->left;
                }
                $index++;
            }
            if ($index < count($values)) {
                if ($values[$index] !== null) {
                    $node->right = (object)['val' => $values[$index], 'left' => null, 'right' => null];
                    $queue[] = $node->right;
                }
                $index++;
            }
        }
        return $root;
    }

    private function merge($node, &$valueToRoot) {
        if ($node === null) {
            return true;
        }
        if ($node->left !== null && isset($valueToRoot[$node->left->val])) {
            $key = $node->left->val;
            $node->left = $valueToRoot[$key];
            unset($valueToRoot[$key]);
        }
        if ($node->right !== null && isset($valueToRoot[$node->right->val])) {
            $key = $node->right->val;
            $node->right = $valueToRoot[$key];
            unset($valueToRoot[$key]);
        }
        return $this->merge($node->left, $valueToRoot) && $this->merge($node->right, $valueToRoot);
    }

    private function isValidBST($node, $lo, $hi) {
        if ($node === null) {
            return true;
        }
        if ($node->val <= $lo || $node->val >= $hi) {
            return false;
        }
        return $this->isValidBST($node->left, $lo, $node->val)
            && $this->isValidBST($node->right, $node->val, $hi);
    }
}
