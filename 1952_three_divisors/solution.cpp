// LeetCode 1952 - Three Divisors
class Solution {
public:
    bool isThree(int n) {
        int root = 0;
        while ((root + 1) * (root + 1) <= n) root++;
        if (root * root != n || root < 2) return false;
        for (int i = 2; i * i <= root; i++) if (root % i == 0) return false;
        return true;
    }
};
