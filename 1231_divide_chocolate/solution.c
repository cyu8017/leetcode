// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

int maximizeSweetness(int* sweetness, int sweetnessSize, int k) {
    int total = 0;
    for (int i = 0; i < sweetnessSize; i++) total += sweetness[i];
    int lo = 1, hi = total / (k + 1);
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int pieces = 0;
        int current = 0;
        for (int i = 0; i < sweetnessSize; i++) {
            current += sweetness[i];
            if (current >= mid) {
                pieces++;
                current = 0;
            }
        }
        if (pieces >= k + 1) lo = mid + 1;
        else hi = mid - 1;
    }
    return hi;
}
