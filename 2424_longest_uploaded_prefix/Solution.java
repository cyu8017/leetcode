// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix {
    private boolean[] uploaded;
    private int prefixLen;

    public LUPrefix(int n) {
        uploaded = new boolean[n + 2];
        prefixLen = 0;
    }

    public void upload(int video) {
        uploaded[video] = true;
        while (uploaded[prefixLen + 1]) prefixLen++;
    }

    public int longest() {
        return prefixLen;
    }
}
