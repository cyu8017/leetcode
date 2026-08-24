# LeetCode 2759 - Convert JSON String to Object
# https://leetcode.com/problems/convert-json-string-to-object/

# @param {String} s
# @return {Object}
def json_parse(s)
  i = 0
  parse = lambda do
    if s[i] == '"'
      i += 1
      out = +""
      while s[i] != '"'
        out << s[i]
        i += 1
      end
      i += 1
      return out
    end
    if s[i] == "t"
      i += 4
      return true
    end
    if s[i] == "f"
      i += 5
      return false
    end
    if s[i] == "n"
      i += 4
      return nil
    end
    if s[i] == "["
      i += 1
      arr = []
      if s[i] == "]"
        i += 1
        return arr
      end
      loop do
        arr << parse.call
        if s[i] == ","
          i += 1
          next
        end
        i += 1
        return arr
      end
    end
    if s[i] == "{"
      i += 1
      obj = {}
      if s[i] == "}"
        i += 1
        return obj
      end
      loop do
        key = parse.call
        i += 1
        obj[key] = parse.call
        if s[i] == ","
          i += 1
          next
        end
        i += 1
        return obj
      end
    end
    start = i
    i += 1 if s[i] == "-"
    i += 1 while i < s.length && (s[i] =~ /\d/ || s[i] == ".")
    num = s[start...i]
    num.include?(".") ? num.to_f : num.to_i
  end
  parse.call
end
