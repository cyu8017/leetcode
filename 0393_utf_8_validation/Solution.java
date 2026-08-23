// LeetCode 0393 - UTF-8 Validation

// https://leetcode.com/problems/utf-8-validation/



class Solution {

    public boolean validUtf8(int[] data) {

        int remaining = 0;



        for (int value : data) {

            int byteValue = value & 0xFF;



            if (remaining == 0) {

                if ((byteValue >> 7) == 0b0) {

                    continue;

                }

                if ((byteValue >> 5) == 0b110) {

                    remaining = 1;

                } else if ((byteValue >> 4) == 0b1110) {

                    remaining = 2;

                } else if ((byteValue >> 3) == 0b11110) {

                    remaining = 3;

                } else {

                    return false;

                }

            } else {

                if ((byteValue >> 6) != 0b10) {

                    return false;

                }

                remaining--;

            }

        }



        return remaining == 0;

    }

}
