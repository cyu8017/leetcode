// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

type QueryBatcher struct {
	queryMultiple func([]interface{}) []interface{}
	t             int
	pending       []interface{}
	resolve       []func(interface{})
}

func QueryBatcherConstructor(queryMultiple func([]interface{}) []interface{}, t int) *QueryBatcher {
	return &QueryBatcher{queryMultiple: queryMultiple, t: t}
}

func (this *QueryBatcher) AddQuery(query interface{}, resolve func(interface{})) {
	this.pending = append(this.pending, query)
	this.resolve = append(this.resolve, resolve)
}
