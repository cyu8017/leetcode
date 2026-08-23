// LeetCode 0402 - Remove K Digits

// https://leetcode.com/problems/remove-k-digits/



import java.util.ArrayDeque;

import java.util.Deque;



class Solution {

    public String removeKdigits(String num, int k) {

        Deque<Character> stack = new ArrayDeque<>();



        for (int index = 0; index < num.length(); index++) {

            char digit = num.charAt(index);



            while (k > 0 && !stack.isEmpty() && stack.peekLast() > digit) {

                stack.removeLast();

                k--;

            }

            stack.addLast(digit);

        }



        while (k > 0 && !stack.isEmpty()) {

            stack.removeLast();

            k--;

        }



        StringBuilder result = new StringBuilder();

        for (char digit : stack) {

            result.append(digit);

        }



        int start = 0;

        while (start < result.length() && result.charAt(start) == '0') {

            start++;

        }



        if (start == result.length()) {

            return "0";

        }



        return result.substring(start);

    }

}
