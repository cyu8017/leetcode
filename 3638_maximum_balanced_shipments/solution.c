// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

static int imax(int a,int b){return a>b?a:b;}
int maxBalancedShipments(int* weight, int weightSize) {
    int ans = 0, mx = 0;
    for (int i = 0; i < weightSize; i++) {
        mx = imax(mx, weight[i]);
        if (weight[i] < mx) { ans++; mx = 0; }
    }
    return ans;
}
