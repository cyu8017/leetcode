// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

static const char* WEEKDAYS[] = {
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
};

char* dayOfTheWeek(int day, int month, int year) {
    static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
    year -= month < 3;
    int w = (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7;
    return (char*)WEEKDAYS[w];
}
