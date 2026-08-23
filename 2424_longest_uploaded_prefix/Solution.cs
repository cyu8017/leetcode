// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

public class LUPrefix {
    private bool[] uploaded;
    private int prefixLen;

    public LUPrefix(int n) {
        uploaded = new bool[n + 2];
        prefixLen = 0;
    }

    public void Upload(int video) {
        uploaded[video] = true;
        while (uploaded[prefixLen + 1]) prefixLen++;
    }

    public int Longest() {
        return prefixLen;
    }
}
