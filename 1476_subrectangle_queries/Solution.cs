// LeetCode 1476 - Subrectangle Queries
// https://leetcode.com/problems/subrectangle-queries/

public class SubrectangleQueries {
    int[][] rectangle;
    public SubrectangleQueries(int[][] rectangle) { this.rectangle = rectangle; }
    public void UpdateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int r = row1; r <= row2; r++)
            for (int c = col1; c <= col2; c++)
                rectangle[r][c] = newValue;
    }
    public int GetValue(int row, int col) => rectangle[row][col];
}
