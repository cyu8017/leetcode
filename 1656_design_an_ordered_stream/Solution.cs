// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

using System.Collections.Generic;

public class OrderedStream {
    private readonly string[] a;
    private int p = 1;

    public OrderedStream(int n) {
        a = new string[n + 1];
    }

    public IList<string> Insert(int idKey, string value) {
        a[idKey] = value;
        var output = new List<string>();
        while (p < a.Length && a[p] != null) {
            output.Add(a[p]);
            p++;
        }
        return output;
    }
}
