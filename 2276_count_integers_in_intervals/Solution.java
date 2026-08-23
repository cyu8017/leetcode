// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals {
    private static class SegNode {
        SegNode left, right;
        boolean covered;
    }

    private SegNode root;
    private int cnt;

    private int[] addRange(int L, int R, int l, int r, SegNode[] holder) {
        SegNode node = holder[0];
        if (node == null) {
            node = new SegNode();
            holder[0] = node;
        }
        if (node.covered) return new int[] { 0 };
        if (l <= L && R <= r) {
            node.covered = true;
            node.left = node.right = null;
            return new int[] { R - L + 1 };
        }
        int mid = (L + R) / 2;
        int added = 0;
        if (l <= mid) {
            SegNode[] leftH = new SegNode[] { node.left };
            added += addRange(L, mid, l, r, leftH)[0];
            node.left = leftH[0];
        }
        if (r > mid) {
            SegNode[] rightH = new SegNode[] { node.right };
            added += addRange(mid + 1, R, l, r, rightH)[0];
            node.right = rightH[0];
        }
        if (node.left != null && node.right != null && node.left.covered && node.right.covered) {
            node.covered = true;
            node.left = node.right = null;
        }
        return new int[] { added };
    }

    public CountIntervals() {}

    public void add(int left, int right) {
        SegNode[] holder = new SegNode[] { root };
        cnt += addRange(1, 1_000_000_000, left, right, holder)[0];
        root = holder[0];
    }

    public int count() {
        return cnt;
    }
}
