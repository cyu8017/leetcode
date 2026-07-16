// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree

// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/



public class Solution {

    public bool IsValidSerialization(string preorder) {

        int slots = 1;

        foreach (string node in preorder.Split(',')) {

            slots -= 1;

            if (slots < 0) {

                return false;

            }

            if (node != "#") {

                slots += 2;

            }

        }

        return slots == 0;

    }

}
