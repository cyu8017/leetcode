// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

int totalFruit(int* fruits, int fruitsSize) {
    int count[100001] = {0};
    int kinds = 0, left = 0, ans = 0;
    for (int right = 0; right < fruitsSize; right++) {
        if (count[fruits[right]]++ == 0) kinds++;
        while (kinds > 2) {
            if (--count[fruits[left]] == 0) kinds--;
            left++;
        }
        int len = right - left + 1;
        if (len > ans) ans = len;
    }
    return ans;
}
