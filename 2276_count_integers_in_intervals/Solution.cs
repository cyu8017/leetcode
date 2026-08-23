// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

public class CountIntervals {
    class SegNode {
        public SegNode left, right;
        public bool covered;
    }

    SegNode root;
    int cnt;

    int AddRange(int L, int R, int l, int r, ref SegNode node) {
        if (node == null) node = new SegNode();
        if (node.covered) return 0;
        if (l <= L && R <= r) {
            node.covered = true;
            node.left = node.right = null;
            return R - L + 1;
        }
        int mid = (L + R) / 2;
        int added = 0;
        if (l <= mid) added += AddRange(L, mid, l, r, ref node.left);
        if (r > mid) added += AddRange(mid + 1, R, l, r, ref node.right);
        if (node.left != null && node.right != null && node.left.covered && node.right.covered) {
            node.covered = true;
            node.left = node.right = null;
        }
        return added;
    }

    public CountIntervals() {}

    public void Add(int left, int right) {
        cnt += AddRange(1, 1000000000, left, right, ref root);
    }

    public int Count() { return cnt; }
}
