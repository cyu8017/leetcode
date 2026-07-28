// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

using System;
using System.Collections.Generic;
using System.Globalization;

public class Solution {
    public string MinimizeError(string[] prices, int target) {
        int floors = 0;
        var fracs = new List<double>();
        foreach (string p in prices) {
            double value = double.Parse(p, CultureInfo.InvariantCulture);
            int floor = (int)value;
            floors += floor;
            double frac = value - floor;
            if (frac > 1e-9) {
                fracs.Add(frac);
            }
        }
        int ceilCount = target - floors;
        if (ceilCount < 0 || ceilCount > fracs.Count) {
            return "-1";
        }
        fracs.Sort((a, b) => b.CompareTo(a));
        double error = 0;
        for (int i = 0; i < ceilCount; i++) {
            error += 1 - fracs[i];
        }
        for (int i = ceilCount; i < fracs.Count; i++) {
            error += fracs[i];
        }
        return error.ToString("F3", CultureInfo.InvariantCulture);
    }
}
