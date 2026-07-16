// LeetCode 0316 - Remove Duplicate Letters

// https://leetcode.com/problems/remove-duplicate-letters/



using System.Collections.Generic;

using System.Text;



public class Solution {

    public string RemoveDuplicateLetters(string s) {

        int[] lastIndex = new int[26];

        for (int index = 0; index < s.Length; index++) {

            lastIndex[s[index] - 'a'] = index;

        }



        Stack<char> stack = new();

        HashSet<char> seen = new();

        for (int index = 0; index < s.Length; index++) {

            char ch = s[index];

            if (seen.Contains(ch)) {

                continue;

            }

            while (stack.Count > 0 && stack.Peek() > ch && lastIndex[stack.Peek() - 'a'] > index) {

                seen.Remove(stack.Pop());

            }

            stack.Push(ch);

            seen.Add(ch);

        }



        StringBuilder builder = new();

        foreach (char ch in stack) {

            builder.Append(ch);

        }

        return builder.ToString();

    }

}

