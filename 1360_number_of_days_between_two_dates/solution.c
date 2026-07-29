// LeetCode 1360 - Number of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

static int is_leap(int y) { return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0); }

static int to_days(char* date) {
    int y = (date[0]-'0')*1000 + (date[1]-'0')*100 + (date[2]-'0')*10 + (date[3]-'0');
    int m = (date[5]-'0')*10 + (date[6]-'0');
    int d = (date[8]-'0')*10 + (date[9]-'0');
    int mdays[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    int days = d;
    for (int year = 1971; year < y; year++) days += is_leap(year) ? 366 : 365;
    for (int month = 1; month < m; month++) {
        days += mdays[month];
        if (month == 2 && is_leap(y)) days++;
    }
    return days;
}

int daysBetweenDates(char* date1, char* date2) {
    int a = to_days(date1), b = to_days(date2);
    return a > b ? a - b : b - a;
}
