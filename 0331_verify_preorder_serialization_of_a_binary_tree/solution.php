// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree
// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution {
    /**
     * @param String $preorder
     * @return Boolean
     */
    function isValidSerialization($preorder) {
        return $this->is_valid_serialization($preorder);
    }

    /**
     * @param String $preorder
     * @return Boolean
     */
    function is_valid_serialization($preorder) {
        $slots = 1;
        foreach (explode(",", $preorder) as $node) {
            $slots--;
            if ($slots < 0) {
                return false;
            }
            if ($node !== "#") {
                $slots += 2;
            }
        }
        return $slots === 0;
    }
}
