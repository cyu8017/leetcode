// LeetCode 0385 - Mini Parser

// https://leetcode.com/problems/mini-parser/



import java.util.ArrayList;

import java.util.List;

import java.util.Stack;



class NestedInteger {

    private Integer integer;

    private final List<NestedInteger> list = new ArrayList<>();



    public NestedInteger() {

    }



    public NestedInteger(int value) {

        this.integer = value;

    }



    public boolean isInteger() {

        return integer != null;

    }



    public int getInteger() {

        return integer != null ? integer : 0;

    }



    public List<NestedInteger> getList() {

        return list;

    }

}



class Solution {

    public NestedInteger deserialize(String s) {

        if (s.charAt(0) != '[') {

            return new NestedInteger(Integer.parseInt(s));

        }



        Stack<NestedInteger> stack = new Stack<>();

        NestedInteger current = null;

        int index = 0;

        boolean negative = false;

        int number = 0;

        boolean hasNumber = false;



        while (index < s.length()) {

            char ch = s.charAt(index);

            if (ch == '[') {

                NestedInteger item = new NestedInteger();

                if (current != null) {

                    stack.push(current);

                }

                current = item;

            } else if (ch == '-') {

                negative = true;

            } else if (Character.isDigit(ch)) {

                number = number * 10 + (ch - '0');

                hasNumber = true;

            } else if (ch == ',' || ch == ']') {

                if (hasNumber) {

                    current.getList().add(new NestedInteger(negative ? -number : number));

                    number = 0;

                    negative = false;

                    hasNumber = false;

                }

                if (ch == ']') {

                    if (stack.isEmpty()) {

                        return current;

                    }

                    NestedInteger parent = stack.pop();

                    parent.getList().add(current);

                    current = parent;

                }

            }

            index++;

        }



        return current != null ? current : new NestedInteger();

    }

}
