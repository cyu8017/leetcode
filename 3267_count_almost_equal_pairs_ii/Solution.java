// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution {
    private String sa;
    private String sb;

    public int countPairs(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (almostEqual(nums[i], nums[j])) ans++;
            }
        }
        return ans;
    }

    private String padNum(int x) {
        if (x == 0) return "0";
        StringBuilder b = new StringBuilder();
        while (x > 0) {
            b.insert(0, (char) ('0' + x % 10));
            x /= 10;
        }
        return b.toString();
    }

    private boolean almostEqual(int a, int b) {
        sa = padNum(a);
        sb = padNum(b);
        while (sa.length() < sb.length()) sa = "0" + sa;
        while (sb.length() < sa.length()) sb = "0" + sb;
        if (sa.equals(sb)) return true;
        return canWithSwaps(2);
    }

    private boolean canWithSwaps(int maxSwap) {
        char[] arr = sa.toCharArray();
        return dfs(arr, 0, maxSwap);
    }

    private boolean dfs(char[] arr, int start, int left) {
        if (new String(arr).equals(sb)) return true;
        if (left == 0) return false;
        for (int i = start; i < arr.length; i++) {
            if (arr[i] == sb.charAt(i)) continue;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] == sb.charAt(i)) {
                    char tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
                    if (dfs(arr, i + 1, left - 1)) return true;
                    tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
                }
            }
            return false;
        }
        return new String(arr).equals(sb);
    }
}
