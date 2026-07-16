// LeetCode 0420 - Strong Password Checker

// https://leetcode.com/problems/strong-password-checker/



public class Solution {

    public int StrongPasswordChecker(string password) {

        int length = password.Length;

        int missing = 3;



        if (password.Any(char.IsLower)) {

            missing--;

        }



        if (password.Any(char.IsUpper)) {

            missing--;

        }



        if (password.Any(char.IsDigit)) {

            missing--;

        }



        int replace = 0;

        int oneRepeat = 0;

        int twoRepeat = 0;

        int index = 0;



        while (index < length) {

            int run = 1;



            while (index + run < length && password[index + run] == password[index]) {

                run++;

            }



            if (run >= 3) {

                replace += run / 3;



                if (run % 3 == 0) {

                    oneRepeat++;

                } else if (run % 3 == 1) {

                    twoRepeat++;

                }

            }



            index += run;

        }



        if (length < 6) {

            return Math.Max(6 - length, missing);

        }



        if (length <= 20) {

            return Math.Max(missing, replace);

        }



        int delete = length - 20;

        replace -= Math.Min(delete, oneRepeat);

        delete -= Math.Min(delete, oneRepeat);

        replace -= Math.Min(delete / 2, twoRepeat);

        delete -= Math.Min(delete / 2, twoRepeat) * 2;

        replace -= delete / 3;



        return length - 20 + Math.Max(missing, replace);

    }

}
