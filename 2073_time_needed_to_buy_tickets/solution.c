// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    int ans = 0;
    for (int i = 0; i < ticketsSize; i++) {
        if (i <= k) ans += tickets[i] < tickets[k] ? tickets[i] : tickets[k];
        else ans += tickets[i] < tickets[k] ? tickets[i] : tickets[k] - 1;
    }
    return ans;
}
