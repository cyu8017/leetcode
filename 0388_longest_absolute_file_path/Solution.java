// LeetCode 0388 - Longest Absolute File Path

// https://leetcode.com/problems/longest-absolute-file-path/



import java.util.ArrayDeque;

import java.util.Deque;



class Solution {

    public int lengthLongestPath(String input) {

        Deque<Integer> stack = new ArrayDeque<>();

        int maxLength = 0;



        for (String line : input.split("\n", -1)) {

            int depth = 0;

            while (depth < line.length() && line.charAt(depth) == '\t') {

                depth++;

            }

            String name = line.substring(depth);



            while (stack.size() > depth) {

                stack.removeLast();

            }



            if (name.contains(".")) {

                int prefix = stack.isEmpty() ? 0 : stack.peekLast();

                maxLength = Math.max(maxLength, prefix + name.length());

            } else {

                int prefix = stack.isEmpty() ? 0 : stack.peekLast();

                stack.addLast(prefix + name.length() + 1);

            }

        }



        return maxLength;

    }

}
