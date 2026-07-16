// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree

// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/



class Solution {

    fun isValidSerialization(preorder: String): Boolean {

        var slots = 1

        for (node in preorder.split(",")) {

            slots -= 1

            if (slots < 0) {

                return false

            }

            if (node != "#") {

                slots += 2

            }

        }

        return slots == 0

    }

}
