// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

int minimumIndex(int* capacity, int capacitySize, int itemSize) {
    int ans = -1;
    for (int i = 0; i < capacitySize; i++) {
        if (capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans])) ans = i;
    }
    return ans;
}
