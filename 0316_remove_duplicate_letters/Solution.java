// LeetCode 0316 - Remove Duplicate Letters

// https://leetcode.com/problems/remove-duplicate-letters/



import java.util.ArrayDeque;

import java.util.Deque;

import java.util.HashSet;

import java.util.Set;



class Solution {

    public String removeDuplicateLetters(String s) {

        int[] lastIndex = new int[26];

        for (int index = 0; index < s.length(); index++) {

            lastIndex[s.charAt(index) - 'a'] = index;

        }



        Deque<Character> stack = new ArrayDeque<>();

        Set<Character> seen = new HashSet<>();

        for (int index = 0; index < s.length(); index++) {

            char ch = s.charAt(index);

            if (seen.contains(ch)) {

                continue;

            }

            while (!stack.isEmpty() && stack.peekLast() > ch

                    && lastIndex[stack.peekLast() - 'a'] > index) {

                seen.remove(stack.removeLast());

            }

            stack.addLast(ch);

            seen.add(ch);

        }



        StringBuilder builder = new StringBuilder();

        for (char ch : stack) {

            builder.append(ch);

        }

        return builder.toString();

    }

}

