// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

int maxSatisfied(int* customers, int customersSize, int* grumpy, int grumpySize, int minutes) {
    (void)grumpySize;
    int base = 0;
    for (int i = 0; i < customersSize; i++) {
        if (grumpy[i] == 0) {
            base += customers[i];
        }
    }
    int gain = 0, best = 0;
    for (int i = 0; i < customersSize; i++) {
        if (grumpy[i]) {
            gain += customers[i];
        }
        if (i >= minutes && grumpy[i - minutes]) {
            gain -= customers[i - minutes];
        }
        if (gain > best) {
            best = gain;
        }
    }
    return base + best;
}
