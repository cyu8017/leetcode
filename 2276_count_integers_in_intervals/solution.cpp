// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

struct SegNode {
    SegNode *left = nullptr, *right = nullptr;
    bool covered = false;
};

class CountIntervals {
    SegNode* root = nullptr;
    int cnt = 0;

    int add(int L, int R, int l, int r, SegNode*& node) {
        if (!node) node = new SegNode();
        if (node->covered) return 0;
        if (l <= L && R <= r) {
            node->covered = true;
            node->left = node->right = nullptr;
            return R - L + 1;
        }
        int mid = (L + R) / 2;
        int added = 0;
        if (l <= mid) added += add(L, mid, l, r, node->left);
        if (r > mid) added += add(mid + 1, R, l, r, node->right);
        if (node->left && node->right && node->left->covered && node->right->covered) {
            node->covered = true;
            node->left = node->right = nullptr;
        }
        return added;
    }
public:
    CountIntervals() {}

    void add(int left, int right) {
        cnt += add(1, 1000000000, left, right, root);
    }

    int count() { return cnt; }
};
