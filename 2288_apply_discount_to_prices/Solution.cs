// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

using System;
using System.Globalization;
using System.Text;

public class Solution {
    public string DiscountPrices(string sentence, int discount) {
        string[] parts = sentence.Split(' ');
        for (int i = 0; i < parts.Length; i++) {
            string part = parts[i];
            if (part.Length >= 2 && part[0] == '$') {
                bool ok = true;
                for (int j = 1; j < part.Length; j++)
                    if (part[j] < '0' || part[j] > '9') { ok = false; break; }
                if (ok) {
                    long val = long.Parse(part.Substring(1));
                    double price = val * (100.0 - discount) / 100.0;
                    parts[i] = "$" + price.ToString("F2", CultureInfo.InvariantCulture);
                }
            }
        }
        return string.Join(" ", parts);
    }
}
