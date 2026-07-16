class Solution:
    def processQueries(self, queries, m):
        values = list(range(1, m + 1))
        answer = []
        for query in queries:
            index = values.index(query)
            answer.append(index)
            values.insert(0, values.pop(index))
        return answer
