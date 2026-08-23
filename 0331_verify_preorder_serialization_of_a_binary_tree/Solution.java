// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree

// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/



class Solution {

    public boolean isValidSerialization(String preorder) {

        int slots = 1;

        for (String node : preorder.split(",")) {

            slots -= 1;

            if (slots < 0) {

                return false;

            }

            if (!node.equals("#")) {

                slots += 2;

            }

        }

        return slots == 0;

    }

}
