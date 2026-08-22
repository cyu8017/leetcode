// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

enum { N3881 = 100001, MOD3881 = 1000000007 };
static long long f3881[N3881], g3881[N3881];
static int inited3881 = 0;

static long long qmi3881(long long a, long long k, long long p) {
    long long res = 1;
    while (k) {
        if (k & 1) res = res * a % p;
        k >>= 1;
        a = a * a % p;
    }
    return res;
}

static void init3881(void) {
    if (inited3881) return;
    f3881[0] = g3881[0] = 1;
    for (int i = 1; i < N3881; i++) {
        f3881[i] = f3881[i - 1] * i % MOD3881;
        g3881[i] = qmi3881(f3881[i], MOD3881 - 2, MOD3881);
    }
    inited3881 = 1;
}

static long long comb3881(int n, int k) {
    return f3881[n] * g3881[k] % MOD3881 * g3881[n - k] % MOD3881;
}

int countVisiblePeople(int n, int pos, int k) {
    init3881();
    int l = pos, r = n - pos - 1;
    long long ans = 0;
    int lim = k < l ? k : l;
    for (int a = 0; a <= lim; a++) {
        int b = k - a;
        if (b <= r) {
            ans = (ans + 2 * comb3881(l, a) % MOD3881 * comb3881(r, b) % MOD3881) % MOD3881;
        }
    }
    return (int)ans;
}
