// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

long long waysToBuyPensPencils(int total, int cost1, int cost2) {
    long long ans = 0;
    for (int pens = 0; pens * cost1 <= total; pens++) {
        int remain = total - pens * cost1;
        ans += (long long)(remain / cost2) + 1;
    }
    return ans;
}
