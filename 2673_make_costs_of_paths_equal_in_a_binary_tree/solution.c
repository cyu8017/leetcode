// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

static int abs2673(int x) { return x < 0 ? -x : x; }

int minIncrements(int n, int* cost, int costSize) {
    (void)costSize;
    int ans = 0;
    for (int i = n / 2 - 1; i >= 0; i--) {
        int l = 2 * i + 1, r = 2 * i + 2;
        ans += abs2673(cost[l] - cost[r]);
        if (cost[l] > cost[r]) cost[i] += cost[l];
        else cost[i] += cost[r];
    }
    return ans;
}
