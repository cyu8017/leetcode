// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

class Solution {
    public String convertDateToBinary(String date) {
        String[] parts = date.split("-");
        int y = Integer.parseInt(parts[0]), m = Integer.parseInt(parts[1]), d = Integer.parseInt(parts[2]);
        return toBinary(y) + "-" + toBinary(m) + "-" + toBinary(d);
    }

    private String toBinary(int v) {
        if (v == 0) return "0";
        StringBuilder s = new StringBuilder();
        while (v > 0) {
            s.insert(0, (char) ('0' + (v & 1)));
            v >>= 1;
        }
        return s.toString();
    }
}
