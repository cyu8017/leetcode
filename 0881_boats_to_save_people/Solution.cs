// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

using System;

public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        Array.Sort(people);
        int i = 0, j = people.Length - 1, boats = 0;
        while (i <= j) {
            if (people[i] + people[j] <= limit) i++;
            j--;
            boats++;
        }
        return boats;
    }
}
