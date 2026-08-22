// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

int hIndex(int* citations, int citationsSize) {
    int* buckets = (int*)calloc((size_t)citationsSize + 1, sizeof(int));
    for (int i = 0; i < citationsSize; i++) {
        int index = citations[i];
        if (index > citationsSize) {
            index = citationsSize;
        }
        buckets[index]++;
    }
    int total = 0;
    for (int h = citationsSize; h >= 0; h--) {
        total += buckets[h];
        if (total >= h) {
            free(buckets);
            return h;
        }
    }
    free(buckets);
    return 0;
}
