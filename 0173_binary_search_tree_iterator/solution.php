// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

class TreeNode {
    public int $val;
    public ?TreeNode $left;
    public ?TreeNode $right;

    function __construct(int $val = 0, ?TreeNode $left = null, ?TreeNode $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class BSTIterator {
    private array $stack = [];

    function __construct(?TreeNode $root) {
        $this->pushLeft($root);
    }

    function next(): int {
        $node = array_pop($this->stack);
        $this->pushLeft($node->right);
        return $node->val;
    }

    function hasNext(): bool {
        return !empty($this->stack);
    }

    private function pushLeft(?TreeNode $node): void {
        while ($node !== null) {
            $this->stack[] = $node;
            $node = $node->left;
        }
    }
}