// LeetCode 0333 - Largest BST Subtree
// https://leetcode.com/problems/largest-bst-subtree/

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
    private $best = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function largestBSTSubtree($root) {
        return $this->largest_bst_subtree($root);
    }

    /**
     * @param TreeNode|array|null $root
     * @return Integer
     */
    function largest_bst_subtree($root) {
        if (is_array($root)) {
            $root = $this->listToTree($root);
        }
        $this->best = 0;
        $this->dfs($root);
        return $this->best;
    }

    private function dfs($node) {
        if ($node === null) {
            return [true, PHP_INT_MAX, PHP_INT_MIN, 0];
        }

        [$leftOk, $leftMin, $leftMax, $leftSize] = $this->dfs($node->left);
        [$rightOk, $rightMin, $rightMax, $rightSize] = $this->dfs($node->right);

        if ($leftOk && $rightOk && $leftMax < $node->val && $node->val < $rightMin) {
            $size = $leftSize + $rightSize + 1;
            $this->best = max($this->best, $size);
            return [true, min($leftMin, $node->val), max($rightMax, $node->val), $size];
        }

        return [false, 0, 0, 0];
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
