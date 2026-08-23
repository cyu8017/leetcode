// LeetCode 0401 - Binary Watch

// https://leetcode.com/problems/binary-watch/



using System.Collections.Generic;



public class Solution {

    public IList<string> ReadBinaryWatch(int turnedOn) {

        List<string> result = new();



        for (int hour = 0; hour < 12; hour++) {

            for (int minute = 0; minute < 60; minute++) {

                if (BitCount(hour) + BitCount(minute) == turnedOn) {

                    result.Add($"{hour}:{minute:D2}");

                }

            }

        }



        return result;

    }



    private static int BitCount(int value) {

        int count = 0;

        while (value != 0) {

            count += value & 1;

            value >>= 1;

        }

        return count;

    }

}
