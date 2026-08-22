// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

static int toDay(const char* s) {
    int days[] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int m = (s[0]-'0')*10 + (s[1]-'0');
    int d = (s[3]-'0')*10 + (s[4]-'0');
    int res = d;
    for (int i = 0; i < m - 1; i++) res += days[i];
    return res;
}

int countDaysTogether(char* arriveAlice, char* leaveAlice, char* arriveBob, char* leaveBob) {
    int a1 = toDay(arriveAlice), a2 = toDay(leaveAlice);
    int b1 = toDay(arriveBob), b2 = toDay(leaveBob);
    int start = a1 > b1 ? a1 : b1;
    int end = a2 < b2 ? a2 : b2;
    if (end < start) return 0;
    return end - start + 1;
}
