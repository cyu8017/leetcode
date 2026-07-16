class Solution
  def partition(s)
    result = []
    path = []

    is_palindrome = lambda do |left, right|
      while left < right
        return false if s[left] != s[right]

        left += 1
        right -= 1
      end
      true
    end

    dfs = lambda do |start|
      if start == s.length
        result << path.dup
        next
      end

      (start...s.length).each do |finish|
        next unless is_palindrome.call(start, finish)

        path << s[start..finish]
        dfs.call(finish + 1)
        path.pop
      end
    end

    dfs.call(0)
    result
  end
end