// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

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
        $parts = [];
        $this->preorder($root, $parts);
        return implode(",", $parts);
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
        $index = 0;
        return $this->build($values, $index);
    }

    private function preorder($node, &$parts) {
        if ($node === null) {
            $parts[] = "#";
            return;
        }
        $parts[] = (string)$node->val;
        $this->preorder($node->left, $parts);
        $this->preorder($node->right, $parts);
    }

    private function build($values, &$index) {
        if ($index >= count($values) || $values[$index] === "#") {
            $index++;
            return null;
        }
        $node = new TreeNode((int)$values[$index]);
        $index++;
        $node->left = $this->build($values, $index);
        $node->right = $this->build($values, $index);
        return $node;
    }
}
