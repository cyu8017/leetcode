// LeetCode 0412 - Fizz Buzz

// https://leetcode.com/problems/fizz-buzz/



import java.util.ArrayList;

import java.util.List;



class Solution {

    public List<String> fizzBuzz(int n) {

        List<String> result = new ArrayList<>();



        for (int value = 1; value <= n; value++) {

            if (value % 15 == 0) {

                result.add("FizzBuzz");

            } else if (value % 3 == 0) {

                result.add("Fizz");

            } else if (value % 5 == 0) {

                result.add("Buzz");

            } else {

                result.add(String.valueOf(value));

            }

        }



        return result;

    }

}
