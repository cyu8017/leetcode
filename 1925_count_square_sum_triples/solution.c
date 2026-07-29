// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

int countTriples(int n) {
    int ans = 0;
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            int sum = a * a + b * b;
            for (int c = 1; c <= n; c++) {
                if (c * c == sum) { ans++; break; }
            }
        }
    }
    return ans;
}
