# LeetCode 2408 - Design SQL
# https://leetcode.com/problems/design-sql/

class SQL
  def initialize(names, columns)
    @tables = {}
    @next_id = {}
    @cols = {}
    names.each_index do |i|
      name = names[i]
      @tables[name] = []
      @next_id[name] = 1
      @cols[name] = columns[i]
    end
  end

  def ins(name, row)
    return false unless @tables.key?(name)
    return false if row.length != @cols[name]
    row_id = @next_id[name]
    @next_id[name] = row_id + 1
    full = [row_id.to_s] + row
    @tables[name] << full
    true
  end

  def rmv(name, row_id)
    rows = @tables[name]
    rows.each_index do |i|
      if rows[i][0].to_i == row_id
        rows.delete_at(i)
        return
      end
    end
    nil
  end

  def sel(name, row_id, column_id)
    return "" unless @tables.key?(name)
    @tables[name].each do |r|
      if r[0].to_i == row_id
        return "" if column_id < 1 || column_id >= r.length
        return r[column_id]
      end
    end
    ""
  end

  def exp(name)
    @tables[name].map { |r| r.join(",") }
  end
end
