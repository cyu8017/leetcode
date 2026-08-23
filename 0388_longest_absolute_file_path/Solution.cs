// LeetCode 0388 - Longest Absolute File Path

// https://leetcode.com/problems/longest-absolute-file-path/



using System.Collections.Generic;



public class Solution {

    public int LengthLongestPath(string input) {

        Stack<int> stack = new();

        int maxLength = 0;



        foreach (string line in input.Split('\n')) {

            int depth = 0;

            while (depth < line.Length && line[depth] == '\t') {

                depth++;

            }

            string name = line[depth..];



            while (stack.Count > depth) {

                stack.Pop();

            }



            if (name.Contains('.')) {

                int prefix = stack.Count == 0 ? 0 : stack.Peek();

                maxLength = Math.Max(maxLength, prefix + name.Length);

            } else {

                int prefix = stack.Count == 0 ? 0 : stack.Peek();

                stack.Push(prefix + name.Length + 1);

            }

        }



        return maxLength;

    }

}
