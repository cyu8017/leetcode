// LeetCode 0412 - Fizz Buzz

// https://leetcode.com/problems/fizz-buzz/



public class Solution {

    public IList<string> FizzBuzz(int n) {

        List<string> result = new();



        for (int value = 1; value <= n; value++) {

            if (value % 15 == 0) {

                result.Add("FizzBuzz");

            } else if (value % 3 == 0) {

                result.Add("Fizz");

            } else if (value % 5 == 0) {

                result.Add("Buzz");

            } else {

                result.Add(value.ToString());

            }

        }



        return result;

    }

}
