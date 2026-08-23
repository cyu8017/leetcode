// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

public class Vector2D
{
    private readonly int[][] _vec;
    private int _row;
    private int _col;

    public Vector2D(int[][] vec)
    {
        _vec = vec;
        _row = 0;
        _col = 0;
        Advance();
    }

    public int Next()
    {
        int value = _vec[_row][_col];
        _col += 1;
        Advance();
        return value;
    }

    public bool HasNext()
    {
        Advance();
        return _row < _vec.Length;
    }

    private void Advance()
    {
        while (_row < _vec.Length && _col >= _vec[_row].Length)
        {
            _row += 1;
            _col = 0;
        }
    }
}
