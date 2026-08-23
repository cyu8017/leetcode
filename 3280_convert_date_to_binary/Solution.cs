// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

public class Solution {
    string ToBinary(int v) {
        if (v == 0) return "0";
        var s = new System.Text.StringBuilder();
        while (v > 0) {
            s.Insert(0, (char)('0' + (v & 1)));
            v >>= 1;
        }
        return s.ToString();
    }

    public string ConvertDateToBinary(string date) {
        var parts = date.Split('-');
        int y = int.Parse(parts[0]), m = int.Parse(parts[1]), d = int.Parse(parts[2]);
        return ToBinary(y) + "-" + ToBinary(m) + "-" + ToBinary(d);
    }
}
