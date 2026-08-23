// LeetCode 0420 - Strong Password Checker

// https://leetcode.com/problems/strong-password-checker/



class Solution {

    public int strongPasswordChecker(String password) {

        int length = password.length();

        int missing = 3;



        if (password.chars().anyMatch(Character::isLowerCase)) {

            missing--;

        }



        if (password.chars().anyMatch(Character::isUpperCase)) {

            missing--;

        }



        if (password.chars().anyMatch(Character::isDigit)) {

            missing--;

        }



        int replace = 0;

        int oneRepeat = 0;

        int twoRepeat = 0;

        int index = 0;



        while (index < length) {

            int run = 1;



            while (index + run < length && password.charAt(index + run) == password.charAt(index)) {

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

            return Math.max(6 - length, missing);

        }



        if (length <= 20) {

            return Math.max(missing, replace);

        }



        int delete = length - 20;

        replace -= Math.min(delete, oneRepeat);

        delete -= Math.min(delete, oneRepeat);

        replace -= Math.min(delete / 2, twoRepeat);

        delete -= Math.min(delete / 2, twoRepeat) * 2;

        replace -= delete / 3;



        return length - 20 + Math.max(missing, replace);

    }

}
