public class Solution {
    public int[] Read(string file, int[] queries) {
        int[] result = new int[queries.Length];
        int index = 0;
        for (int i = 0; i < queries.Length; i++) {
            int count = System.Math.Min(queries[i], file.Length - index);
            result[i] = count;
            index += count;
        }
        return result;
    }
}