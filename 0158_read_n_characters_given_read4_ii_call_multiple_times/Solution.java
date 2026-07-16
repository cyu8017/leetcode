class Solution {
    public int[] read(String file, int[] queries) {
        int[] result = new int[queries.length];
        int index = 0;
        for (int i = 0; i < queries.length; i++) {
            int count = Math.min(queries[i], file.length() - index);
            result[i] = count;
            index += count;
        }
        return result;
    }
}