# LeetCode 1409 - Queries On A Permutation With Key
# https://leetcode.com/problems/queries-on-a-permutation-with-key/

def process_queries(queries, m)
  values = (1..m).to_a
  queries.map do |query|
    index = values.index(query)
    values.unshift(values.delete_at(index))
    index
  end
end
