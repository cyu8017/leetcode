// LeetCode 0394 - Decode String

// https://leetcode.com/problems/decode-string/



import java.util.ArrayDeque;

import java.util.Deque;



class Solution {

    public String decodeString(String s) {

        Deque<String> stack = new ArrayDeque<>();

        StringBuilder current = new StringBuilder();

        int number = 0;



        for (int index = 0; index < s.length(); index++) {

            char character = s.charAt(index);



            if (Character.isDigit(character)) {

                number = number * 10 + (character - '0');

            } else if (character == '[') {

                stack.push(current.toString());

                stack.push(String.valueOf(number));

                current = new StringBuilder();

                number = 0;

            } else if (character == ']') {

                int count = Integer.parseInt(stack.pop());

                String previous = stack.pop();

                StringBuilder repeated = new StringBuilder();

                for (int repeat = 0; repeat < count; repeat++) {

                    repeated.append(current);

                }

                current = new StringBuilder(previous).append(repeated);

            } else {

                current.append(character);

            }

        }



        return current.toString();

    }

}
