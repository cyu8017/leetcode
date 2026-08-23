// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/
// JS QueryBatcher design stand-in.

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;

class QueryBatcher {
    private final Function<int[], int[]> queryMultiple;
    private final int t;
    private final List<Integer> pending = new ArrayList<>();
    private final List<Consumer<Integer>> resolvers = new ArrayList<>();

    public QueryBatcher(Function<int[], int[]> queryMultiple, int t) {
        this.queryMultiple = queryMultiple;
        this.t = t;
    }

    public void addQuery(int query, Consumer<Integer> resolve) {
        pending.add(query);
        resolvers.add(resolve);
    }
}
