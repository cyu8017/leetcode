// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

using System;

public class Solution {
    public string ReformatDate(string date) {
        string[] months = { "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec" };
        string[] parts = date.Split(' ');
        int day = int.Parse(parts[0].Substring(0, parts[0].Length - 2));
        int month = Array.IndexOf(months, parts[1]) + 1;
        return $"{parts[2]}-{month:D2}-{day:D2}";
    }
}
