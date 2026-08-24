# LeetCode 2756 - Query Batching
# https://leetcode.com/problems/query-batching/

class QueryBatcher
  def initialize(query_multiple, t)
    @query_multiple = query_multiple
    @t = t
    @pending = []
    @busy_until = 0
  end

  def get_value(key)
    @pending << key
    keys = @pending
    @pending = []
    @busy_until += @t
    result = @query_multiple.call(keys)
    result.is_a?(Array) ? result[0] : result
  end

  def getValue(key)
    get_value(key)
  end
end
