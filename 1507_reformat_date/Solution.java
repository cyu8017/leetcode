// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

class Solution {
    private static final String[] MONTHS = {
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    };

    public String reformatDate(String date) {
        String[] parts = date.split(" ");
        String day = parts[0];
        String month = parts[1];
        String year = parts[2];

        int monthIndex = 0;
        for (int i = 0; i < MONTHS.length; i++) {
            if (MONTHS[i].equals(month)) {
                monthIndex = i + 1;
                break;
            }
        }

        int dayValue = Integer.parseInt(day.substring(0, day.length() - 2));
        return String.format("%s-%02d-%02d", year, monthIndex, dayValue);
    }
}
