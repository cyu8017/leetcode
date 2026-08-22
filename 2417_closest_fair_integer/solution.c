// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

int closestFair(int n) {
    for (int x = n; ; x++) {
        int tmp = x, digits = 0, even = 0, odd = 0;
        if (tmp == 0) digits = 1;
        int vals[20], vc = 0;
        int t = x;
        if (t == 0) vals[vc++] = 0;
        while (t > 0) { vals[vc++] = t % 10; t /= 10; }
        digits = vc;
        if (digits % 2 != 0) {
            int p = 1;
            for (int i = 0; i < digits; i++) p *= 10;
            return closestFair(p);
        }
        for (int i = 0; i < vc; i++) {
            if (vals[i] % 2 == 0) even++; else odd++;
        }
        if (even == odd) return x;
    }
}
