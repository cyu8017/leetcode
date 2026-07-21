
# @param {String} s
# @return {Boolean}
def split_string(s)
  n = s.length

  dfs = lambda do |index, previous, parts|
    return parts >= 2 if index == n

    (index + 1..n).each do |endi|
      value = s[index...endi].to_i
      if previous.nil?
        return true if dfs.call(endi, value, parts + 1)
      elsif value == previous - 1
        return true if dfs.call(endi, value, parts + 1)
      elsif value > previous - 1
        break
      end
    end
    false
  end

  dfs.call(0, nil, 0)
end
